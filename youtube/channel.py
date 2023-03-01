import json
import os
from googleapiclient.discovery import build


class Channel:
    # SKYPROAPIKEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('SKYPROAPIKEY')

    def __init__(self, channel_id):
        """Инициализация по id
        При создании экземпляра инициализируются атрибуты:
        - channel_id: id канала
        - channel_info: информация о канале
        - title: название канала
        - description: описание канала
        - link: ссылка на канал
        - subscriber_count: количество подписчиков
        - video_count: количество видео
        - view_count: количество просмотров"""
        self.__channel_id = channel_id
        channel = self.get_info()
        self.__title = channel['items'][0]['snippet']['title']
        self.__description = channel['items'][0]['snippet']['description']
        self.__url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.__subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.__video_count = channel['items'][0]['statistics']['videoCount']
        self.__views_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __add__(self, other) -> int:
        """Складывает по количеству подписчиков, если второй экземпляр Channel"""
        if not isinstance(other, Channel):
            raise ValueError('Второй объект не Channel')
        return self.subscriber_count + other.subscriber_count

    def __lt__(self, other) -> bool:
        """Сравнивает по количеству подписчиков, если второй экземпляр Channel"""
        if not isinstance(other, Channel):
            raise ValueError('Второй объект не Channel')
        return self.subscriber_count < other.subscriber_count

    @property
    def channel_id(self):
        """Возвращает id"""
        return self.__channel_id

    @property
    def title(self):
        """Возвращает название канала"""
        return self.__title

    @property
    def description(self):
        """Возвращает описание канала"""
        return self.__description

    @property
    def url(self):
        """Возвращает ссылку на канал"""
        return self.__url

    @property
    def subscriber_count(self):
        """Возвращает количество подписчиков"""
        return self.__subscriber_count

    @property
    def video_count(self):
        """Возвращает количество видео"""
        return self.__video_count

    @property
    def views_count(self):
        """Возвращает количество просмотров"""
        return self.__views_count

    @classmethod
    # создать специальный объект для работы с API
    def get_service(cls):
        """Создает и возвращает специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    def get_info(self):
        """Возвращает информацию о канале"""
        channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self):
        """Вывод информации на экран"""
        print(json.dumps(self.get_info(), indent=2, ensure_ascii=False))

    def to_json(self, name):
        """Сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel, в json-файл"""
        with open(name, 'w', encoding='utf-8') as file:
            data = {'id': self.channel_id, 'title': self.title, 'description': self.description,
                    'url': self.url, 'subscriber_count': self.subscriber_count, 'video_count': self.video_count,
                    'views_count': self.views_count}
            json.dump(data, file, indent=2, ensure_ascii=False)


ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # Вдудь
ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')  # Редакция
# получаем значения атрибутов
print(ch1.title)
print(ch1.video_count)
print(ch1.url)

# # менять не можем
# ch1.channel_id = 'Новое название'

# можем получить объект для работы с API вне класса
print(Channel.get_service())

# создать файл 'vdud.json' в данными по каналу
ch1.to_json('vdud.json')
print(ch1)
print(ch2)
print(ch1 + ch2)
print(ch1 > ch2)
print(ch1 < ch2)
