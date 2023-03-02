import pytest
import youtube
from youtube.channel import Channel


def test_add(channel_1, channel_2):
    """Ожидается int после сложения экземпляров Channel"""
    assert type(channel_1 + channel_2) is int


def test_add_value_error(channel_1):
    """Ожидается исключение, если складывать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 + 1


def test_lt_(channel_1, channel_2):
    """Ожидается bool после сравнения экземпляров Channel"""
    assert type(channel_1 > channel_2) is bool


def test_lt_value_error(channel_1):
    """Ожидается исключение, если сравнивать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 < 1
        assert channel_1 > 1


def test_get_attributes_channel(channel_1):
    """Ожидается получение str из атрибутов"""
    assert type(channel_1.channel_id) is str
    assert type(channel_1.title) is str
    assert type(channel_1.description) is str
    assert type(channel_1.url) is str
    assert type(channel_1.subscriber_count) is str
    assert type(channel_1.video_count) is str
    assert type(channel_1.views_count) is str


def test_get_service():
    """Ожидается получение объекта для работы с API ютуба"""
    assert Channel.get_service() == youtube.youtube


def test_get_channel(channel_1):
    """Ожидается dict - информация о канале """
    assert type(channel_1.channel) is dict
