import datetime
import isodate
from youtube.basic import Basic


class PlayList(Basic):

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__title = self.playlist['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    def __str__(self):
        return f"Плейлист - '{self.__title}'"

    @property
    def playlist_id(self) -> str:
        """Возвращает id плейлиста"""
        return self.__playlist_id

    @property
    def title(self) -> str:
        """Возвращает название плейлиста"""
        return self.__title

    @property
    def url(self) -> str:
        """Возвращает ссылку на плейлист"""
        return self.__url

    @property
    def playlist(self) -> dict:
        """"""
        return self._get_playlist(playlist_id=self.__playlist_id)

    @property
    def ids_videos(self) -> list:
        """Возвращает список id всех видел в плейлисте"""
        return self._get_ids_videos_in_playlist(playlist_id=self.__playlist_id)

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает общее время плейлиста"""
        return self.get_total_duration()

    def get_total_duration(self) -> datetime.timedelta:
        """Получает общее время плейлиста"""
        videos = self._get_info_video_in_playlist(ids_videos=self.ids_videos)
        total = datetime.timedelta()

        for video in videos['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total += duration

        return total

    def show_best_video(self):
        """Получает ссылку на лучшее видео в плейлисте"""
        videos = self._get_info_video_in_playlist(ids_videos=self.ids_videos)
        best_likes = 0
        best_id = ''
        for video in videos['items']:
            likes = int(video['statistics']['likeCount'])
            if likes > best_likes:
                best_likes = likes
                best_id = video['id']
        return f"Ссылка на лучшее видео в плейлисте:\n" \
               f"https://youtu.be/{best_id}"


# pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
# print(pl.show_best_video())
