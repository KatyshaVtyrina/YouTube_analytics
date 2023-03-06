
def test_str(video_1, video_2):
    assert str(video_1) == f"{video_1.title}"
    assert str(video_2) == f"{video_2.title} ({video_2.playlist_name})"


def test_get_attributes_video(video_1):
    """Ожидается получение str из атрибутов экземпляров Video"""
    assert type(video_1.video_id) is str
    assert type(video_1.title) is str
    assert type(video_1.view_count) is str
    assert type(video_1.like_count) is str


def test_get_attributes_playlist(video_2):
    """Ожидается получение str из атрибутов экземпляров PLVideo"""
    assert type(video_2.video_id) is str
    assert type(video_2.title) is str
    assert type(video_2.playlist_id) is str
    assert type(video_2.channel_id) is str
    assert type(video_2.playlist_name) is str


def test_playlist_of_channel(video_2, video_3):
    """Ожидается информация о нахождении видео в плейлисте"""
    assert (video_2.check_video_in_playlist()) == f"Видео '{video_2.title}' есть в плейлисте '{video_2.playlist_name}'"
    assert (video_3.check_video_in_playlist()) == f"Видео '{video_3.title}' нет в плейлисте '{video_3.playlist_name}'"
