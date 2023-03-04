import datetime

import pytest
from youtube.basic import Basic


def test_get_attributes_playlist(playlist_1):
    """Ожидается получение str из атрибутов"""
    assert type(playlist_1.playlist_id) is str
    assert type(playlist_1.title) is str
    assert type(playlist_1.url) is str


def test_get_total_duration(playlist_1):
    assert type(playlist_1.total_duration) is datetime.timedelta


def test_show_best_video(playlist_1):
    """Ожидается получение str от функции, возвращающей ссылку на лучшее видео"""
    assert type(playlist_1.show_best_video()) is str

