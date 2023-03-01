import json
from youtube import youtube


class Video:

    def __init__(self, video_id):
        """Инициализируется по id
        После создания экземпляра инициализируются атрибуты:
        - название видео(title)
        - количество просмотров(view_count)
        - количество лайков(like_count)"""
        self.__video_id = video_id
        self.__title = self.info_video['items'][0]['snippet']['localized']['title']
        self.__view_count = self.info_video['items'][0]['statistics']['viewCount']
        self.__like_count = self.info_video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.__title

    @property
    def video_id(self):
        """Возвращает id"""
        return self.__video_id

    @property
    def info_video(self) -> dict:
        """Возвращает словарь с данными по видео"""
        return self.get_video(self.__video_id)

    @property
    def title(self) -> str:
        """Возвращает название видео"""
        return self.__title

    @property
    def view_count(self) -> str:
        """Возвращает количество просмотров"""
        return self.__view_count

    @property
    def like_count(self) -> str:
        """Возвращает количество лайков"""
        return self.__like_count

    @classmethod
    def get_video(cls, video_id) -> dict:
        """Получает данные о видео """
        video = youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        return video

    def print_info_video(self) -> json:
        """Вывод информации на экран"""
        print(json.dumps(self.info_video, indent=2, ensure_ascii=False))


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        """Дополнительно инициализируется название плейлиста"""
        super().__init__(video_id)
        self.__playlist_id = playlist_id
        self.__playlist_name = self.info_playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f"{super().__str__()} ({self.__playlist_name})"

    @property
    def playlist_id(self) -> str:
        """Возвращает id плейлиста"""
        return self.__playlist_id

    @property
    def playlist_name(self) -> str:
        """Возвращает имя плейлиста"""
        return self.__playlist_name

    @property
    def info_playlist(self) -> dict:
        """Возвращает словарь с данными по плейлисту"""
        return self.get_playlist(self.__playlist_id)

    @classmethod
    def get_playlist(cls, playlist_id) -> dict:
        """Получает данные о плейлисте"""
        playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        return playlist

    def print_info_playlist(self) -> json:
        """Вывод информации на экран"""
        print(json.dumps(self.info_playlist, indent=2, ensure_ascii=False))


video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video1)
print(video2)
