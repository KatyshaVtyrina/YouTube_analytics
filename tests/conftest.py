import pytest

from youtube.channel import Channel
from youtube.playlist import PlayList
from youtube.video import PLVideo, Video


@pytest.fixture
def channel_1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def channel_2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')


@pytest.fixture
def video_1():
    return Video('9lO06Zxhu88')


@pytest.fixture
def video_2():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


@pytest.fixture
def video_3():
    return PLVideo('9lO06Zxhu88', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


@pytest.fixture
def video_4():
    return Video('broken_video_id')


@pytest.fixture
def playlist_1():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


@pytest.fixture
def path():
    return 'tests/test_data/test_to_json.json'