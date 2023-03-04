import json
import googleapiclient
import pytest
from youtube.basic import Basic


def test_get_value_error():
    with pytest.raises(ValueError):
        Basic()


def test_get_service():
    """Ожидается получение объекта для работы с API ютуба"""
    assert type(Basic.get_service()) is googleapiclient.discovery.Resource


def test_get_channel(channel_1):
    """Ожидается dict - информация о канале """
    assert type(channel_1.channel) is dict


def test_get_video(video_1):
    """Ожидается dict - информация о видео"""
    assert type(video_1.info_video) is dict


def test_get_playlist(video_2):
    """Ожидается dict - информация плейлисте"""
    assert type(video_2.playlist) is dict


def test_get_playlist_channel(video_2):
    """Ожидается dict - информация о плейлисте канала"""
    assert type(video_2.playlist_channel) is dict


def test_get_id_videos_in_playlist(playlist_1):
    """Ожидается dict - информация о плейлисте канала"""
    assert type(Basic._get_id_videos_in_playlist(playlist_id=playlist_1.playlist_id)) is list


def test_get_info_video_in_playlist(playlist_1):
    """Ожидается dict - информация о плейлисте канала"""
    assert type(playlist_1._get_info_video_in_playlist(ids_videos=playlist_1.ids_videos)) is dict


def test_print_info():
    data = {'One': True, '2': 'Two'}
    data_json = Basic._print_info(data)
    assert json.loads(data_json) == data
