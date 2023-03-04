import json

from youtube.basic import Basic


class Channel(Basic):

    def __init__(self, channel_id: str):
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
        # channel = self.channel(self.__channel_id)
        self.__title = self.channel['items'][0]['snippet']['title']
        self.__description = self.channel['items'][0]['snippet']['description']
        self.__url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.__subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.__video_count = self.channel['items'][0]['statistics']['videoCount']
        self.__views_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __add__(self, other) -> int:
        """Складывает по количеству подписчиков, если второй экземпляр Channel"""
        if not isinstance(other, Channel):
            raise ValueError('Второй объект не Channel')
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __lt__(self, other) -> bool:
        """Сравнивает по количеству подписчиков, если второй экземпляр Channel"""
        if not isinstance(other, Channel):
            raise ValueError('Второй объект не Channel')
        return self.subscriber_count < other.subscriber_count

    def __gt__(self, other) -> bool:
        """Сравнивает по количеству подписчиков, если второй экземпляр Channel"""
        if not isinstance(other, Channel):
            raise ValueError('Второй объект не Channel')
        return self.subscriber_count > other.subscriber_count

    @property
    def channel_id(self) -> str:
        """Возвращает id"""
        return self.__channel_id

    @property
    def title(self) -> str:
        """Возвращает название канала"""
        return self.__title

    @property
    def description(self) -> str:
        """Возвращает описание канала"""
        return self.__description

    @property
    def url(self) -> str:
        """Возвращает ссылку на канал"""
        return self.__url

    @property
    def subscriber_count(self) -> str:
        """Возвращает количество подписчиков"""
        return self.__subscriber_count

    @property
    def video_count(self) -> str:
        """Возвращает количество видео"""
        return self.__video_count

    @property
    def views_count(self) -> str:
        """Возвращает количество просмотров"""
        return self.__views_count

    @property
    def channel(self) -> dict:
        """Возвращает информацию о канале"""
        return self._get_channel(channel_id=self.__channel_id)

    def print_info(self) -> json:
        """Вывод информации на экран"""
        print(super()._print_info(data=self.channel))

    def to_json(self, name: str) -> json:
        """Сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel, в json-файл"""
        with open(name, 'w', encoding='utf-8') as file:
            data = {'id': self.channel_id, 'title': self.title, 'description': self.description,
                    'url': self.url, 'subscriber_count': self.subscriber_count, 'video_count': self.video_count,
                    'views_count': self.views_count}
            json.dump(data, file, indent=2, ensure_ascii=False)
