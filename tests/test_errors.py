from youtube.errors import YoutubeApiError


def test_instantiate_csv_error():
    e = YoutubeApiError()
    assert (str(e)) == "Неизвестная ошибка"
