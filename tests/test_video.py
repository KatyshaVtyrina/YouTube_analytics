
def test_str(video_1, video_2):
    assert str(video_1) == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"
    assert str(video_2) == "Пушкин: наше все? (Литература)"

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
    assert (video_2.check_video_in_playlist()) == "Видео 'Пушкин: наше все?' есть в плейлисте 'Литература'"
    assert (video_3.check_video_in_playlist()) == "Видео 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)' нет в плейлисте 'Литература'"