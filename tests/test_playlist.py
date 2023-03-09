import datetime


def test_str(playlist_1):
    assert str(playlist_1) == f"Плейлист - '{playlist_1.title}'"


def test_get_attributes_playlist(playlist_1):
    """Ожидается получение str из атрибутов"""
    assert isinstance(playlist_1.playlist_id, str)
    assert isinstance(playlist_1.title, str)
    assert isinstance(playlist_1.url, str)


def test_get_total_duration(playlist_1):
    assert isinstance(playlist_1.total_duration, datetime.timedelta)


def test_show_best_video(playlist_1):
    """Ожидается получение str от функции, возвращающей ссылку на лучшее видео"""
    assert isinstance(playlist_1.show_best_video(), str)
