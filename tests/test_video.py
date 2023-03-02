

def test_get_attributes_video(video_1):
    """Ожидается получение str из атрибутов экземпляров Video"""
    assert type(video_1.video_id) is str
    assert type(video_1.title) is str
    assert type(video_1.view_count) is str
    assert type(video_1.like_count) is str


def test_get_video(video_1):
    """Ожидается dict - информация о видео"""
    assert type(video_1.info_video) is dict


def test_get_attributes_playlist(video_2):
    """Ожидается получение str из атрибутов экземпляров PLVideo"""
    assert type(video_2.video_id) is str
    assert type(video_2.title) is str
    assert type(video_2.playlist_id) is str
    assert type(video_2.channel_id) is str
    assert type(video_2.playlist_name) is str


def test_get_playlist(video_2):
    """Ожидается dict - информация плейлисте"""
    assert type(video_2.playlist) is dict


def test_get_playlist_channel(video_2):
    """Ожидается dict - информация о плейлисте канала"""
    assert type(video_2.playlist_channel) is dict


def test_print_info_playlist():
    pass


def test_print_playlist_of_channel():
    pass
