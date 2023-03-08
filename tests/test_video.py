import json


def test_str(video_1, video_2):
    assert str(video_1) == f"{video_1.title}"
    assert str(video_2) == f"{video_2.title} ({video_2.playlist_name})"


def test_get_attributes_video(video_1):
    """Ожидается получение str из атрибутов экземпляров Video"""
    assert isinstance(video_1.video_id, str)
    assert isinstance(video_1.title, str)
    assert isinstance(video_1.view_count, str)
    assert isinstance(video_1.like_count, str)


def test_wrong_id(video_4):
    """Ожидается инициализация только video_id"""
    assert video_4.video_id == "broken_video_id"
    assert video_4.title is None
    assert video_4.like_count is None
    assert video_4.view_count is None


def test_get_attributes_playlist(video_2):
    """Ожидается получение str из атрибутов экземпляров PLVideo"""
    assert isinstance(video_2.video_id, str)
    assert isinstance(video_2.title, str)
    assert isinstance(video_2.playlist_id, str)
    assert isinstance(video_2.channel_id, str)
    assert isinstance(video_2.playlist_name, str)


def test_playlist_of_channel(video_2, video_3):
    """Ожидается информация о нахождении видео в плейлисте"""
    assert (video_2.check_video_in_playlist()) == f"Видео '{video_2.title}' есть в плейлисте '{video_2.playlist_name}'"
    assert (video_3.check_video_in_playlist()) == f"Видео '{video_3.title}' нет в плейлисте '{video_3.playlist_name}'"


def test_print_info(video_1):
    json_data = video_1.print_info()
    data = json.loads(json_data)
