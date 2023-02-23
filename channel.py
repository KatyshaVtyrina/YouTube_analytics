import json
import os
from googleapiclient.discovery import build


class Channel:
    # SKYPROAPIKEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('SKYPROAPIKEY')

    def __init__(self, channel_id):
        self.id = channel_id
        self.channel = self.get_service().channels().list(id=self.id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.views_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __add__(self, other) -> int:
        return self.subscriber_count + other.subscriber_count

    def __lt__(self, other) -> bool:
        return self.subscriber_count < other.subscriber_count

    def __gt__(self, other) -> bool:
        return self.subscriber_count > other.subscriber_count

    @property
    def channel_id(self):
        return self.id

    @classmethod
    # создать специальный объект для работы с API
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    def print_info(self):
        # информация о канале
        channel = Channel.get_service().channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, name):
        with open(name, 'w', encoding='utf-8') as file:
            data = {'id': self.id, 'title': self.title, 'description': self.description,
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
