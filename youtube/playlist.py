import datetime
import isodate
from youtube.basic import Basic


class PlayList(Basic):

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__title = self.playlist['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def playlist_id(self):
        return self.__playlist_id

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def playlist(self):
        return self._get_playlist(playlist_id=self.__playlist_id)

    @property
    def ids_videos(self):
        return self._get_id_videos_in_playlist(playlist_id=self.__playlist_id)

    @property
    def total_duration(self):
        return self.get_total_duration()

    def get_total_duration(self):
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


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(type(pl._get_info_video_in_playlist(pl.ids_videos)))