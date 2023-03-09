import json
import pytest


def test_str(channel_1):
    assert str(channel_1) == f'Youtube-канал: {channel_1.title}'


def test_add(channel_1, channel_2):
    """Ожидается int после сложения экземпляров Channel"""
    assert isinstance(channel_1 + channel_2, int)


def test_add_value_error(channel_1):
    """Ожидается исключение, если складывать не с Channel"""
    with pytest.raises(ValueError):
        assert channel_1 + 1


def test_lt(channel_1, channel_2):
    """Ожидается bool после сравнения экземпляров Channel"""
    assert isinstance(channel_1 < channel_2, bool)


def test_gt(channel_1, channel_2):
    """Ожидается bool после сравнения экземпляров Channel"""
    assert isinstance(channel_1 > channel_2, bool)


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
    assert isinstance(channel_1.channel_id, str)
    assert isinstance(channel_1.title, str)
    assert isinstance(channel_1.description, str)
    assert isinstance(channel_1.url, str)
    assert isinstance(channel_1.subscriber_count, str)
    assert isinstance(channel_1.video_count, str)
    assert isinstance(channel_1.views_count, str)


def test_to_json(channel_1, path):
    """Ожидается сохранение информации по каналу в json"""
    channel_1.to_json(path)
    with open(path) as f:
        file = json.load(f)
        assert isinstance(file['id'], str)
        assert isinstance(file['title'], str)
        assert isinstance(file['description'], str)
        assert isinstance(file['url'], str)
        assert isinstance(file['subscriber_count'], str)
        assert isinstance(file['video_count'], str)
        assert isinstance(file['views_count'], str)
