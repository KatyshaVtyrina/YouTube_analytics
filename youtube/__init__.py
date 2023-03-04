import os
from googleapiclient.discovery import build

api_key: str = os.getenv('SKYPROAPIKEY')
youtube = build('youtube', 'v3', developerKey=api_key)
