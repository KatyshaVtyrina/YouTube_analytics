import json
import os
from googleapiclient.discovery import build


class Channel:
    # SKYPROAPIKEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('SKYPROAPIKEY')

    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
