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


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

# получаем значения атрибутов
print(vdud.title)
print(vdud.video_count)
print(vdud.url)

# менять не можем
vdud.channel_id = 'Новое название'

# можем получить объект для работы с API вне класса
print(Channel.get_service())

# создать файл 'vdud.json' в данными по каналу
vdud.to_json('vdud.json')
