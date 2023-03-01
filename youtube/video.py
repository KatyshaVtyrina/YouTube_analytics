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
    def view_count(self):
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

    def print_info(self):
        """Вывод информации на экран"""
        print(json.dumps(self.info_video, indent=2, ensure_ascii=False))


video1 = Video('9lO06Zxhu88')
print(video1)
