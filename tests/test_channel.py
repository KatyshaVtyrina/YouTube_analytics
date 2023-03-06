import json
import pytest


def test_str(channel_1):
    assert str(channel_1) == f'Youtube-канал: {channel_1.title}'


def test_add(channel_1, channel_2):
    """Ожидается int после сложения экземпляров Channel"""
    assert type(channel_1 + channel_2) is int


def test_add_value_error(channel_1):
    """Ожидается исключение, если складывать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 + 1


def test_lt(channel_1, channel_2):
    """Ожидается bool после сравнения экземпляров Channel"""
    assert type(channel_1 < channel_2) is bool


def test_gt(channel_1, channel_2):
    """Ожидается bool после сравнения экземпляров Channel"""
    assert type(channel_1 > channel_2) is bool


def test_lt_value_error(channel_1):
    """Ожидается исключение, если сравнивать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 < 1
    with pytest.raises(ValueError):
        assert 1 < channel_1


def test_gt_value_error(channel_1):
    """Ожидается исключение, если сравнивать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 < 1
    with pytest.raises(ValueError):
        assert 1 < channel_1


def test_get_attributes_channel(channel_1):
    """Ожидается получение str из атрибутов"""
    assert type(channel_1.channel_id) is str
    assert type(channel_1.title) is str
    assert type(channel_1.description) is str
    assert type(channel_1.url) is str
    assert type(channel_1.subscriber_count) is str
    assert type(channel_1.video_count) is str
    assert type(channel_1.views_count) is str


def test_to_json(channel_1, path):
    """Ожидается сохранение информации по каналу в json"""
    channel_1.to_json(path)
    with open(path) as f:
        file = json.load(f)
        assert type(file['id']) is str
        assert type(file['title']) is str
        assert type(file['description']) is str
        assert type(file['url']) is str
        assert type(file['subscriber_count']) is str
        assert type(file['video_count']) is str
        assert type(file['views_count']) is str
