import json
import googleapiclient
import pytest
from youtube.basic import Basic


def test_get_value_error():
    with pytest.raises(ValueError):
        Basic()


def test_get_service():
    """Ожидается получение объекта для работы с API ютуба"""
    assert isinstance(Basic.get_service(), googleapiclient.discovery.Resource)


def test_get_channel(channel_1):
    """Ожидается dict - информация о канале """
    assert isinstance(channel_1.channel, dict)


def test_get_video(video_1):
    """Ожидается dict - информация о видео"""
    assert isinstance(video_1.info_video, dict)


def test_get_playlist(video_2):
    """Ожидается dict - информация плейлисте"""
    assert isinstance(video_2.playlist, dict)


def test_get_playlist_channel(video_2):
    """Ожидается dict - информация о плейлисте канала"""
    assert isinstance(video_2.playlist_channel, dict)


def test_get_ids_videos_in_playlist(playlist_1):
    """Ожидается dict - информация о плейлисте канала"""
    assert isinstance(Basic._get_ids_videos_in_playlist(playlist_id=playlist_1.playlist_id), list)


def test_get_info_video_in_playlist(playlist_1):
    """Ожидается dict - информация о плейлисте канала"""
    assert isinstance(playlist_1._get_info_video_in_playlist(ids_videos=playlist_1.ids_videos), dict)


def test_dict_to_json():
    data = {'One': True, '2': 'Two'}
    data_json = Basic.dict_to_json(data)
    assert json.loads(data_json) == data
