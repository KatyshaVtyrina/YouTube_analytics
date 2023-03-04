Ютуб-аналитика - создание аналога ютуба, в котором тоже будут каналы, плейлисты и видео, но при этом дополненные новой аналитикой.

Сначала необходимо получить ключ для работы с API ютуба и установить его в переменные окружения переменной 'SKYPROAPIKEY'

Класс Channel

Инициализируется айдишником (id) конкретного ютуб-канала.
При создании экземпляра класса происходит инициализация следующих атрибутов класса:
- id канала (id)
- название канала (title)
- описание канала (description)
- ссылка на канал (url)
- количество подписчиков (subscriber_count)
- количество видео (video_count)
- общее количество просмотров (views_count)

У класса есть методы:
print_info() - выводит в консоль информацию о канале.
to_json('<имя файла>') - сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel, в json-файл.
channel - получает информацию о канале

Методы класса:
get_service() - возвращает объект для работы с API ютуба.
get_channel(channel_id) - получает информацию о канале


Класс Video

Инициализируется айдишником (video_id) конкретного видео:
При создании экземпляра класса происходит инициализация следующих атрибутов класса:
- название видео (title)
- количество просмотров(view_count)
- количество лайков(like_count)

У класса есть методы:
info_video - Получает данные о видео 
print_info_video - Вывод информации на экран

Методы класса:
get_video(video_id) - Получает данные о видео 


Класс PLVideo наследуется от класса Video

Дополнительно инициализируется id плейлиста(playlist_id)
При создании экземпляра класса дополнительно инициализируются атрибуты:
-название плейлиста(playlist_name)
-id канала(channel_id)

У класса есть методы:

playlist - Возвращает словарь с данными по плейлисту
playlist_channel - Возвращает плейлист канала
print_info_playlist() - Вывод информации о плейлисте
print_playlist_of_channel() - Вывод плейлиста канала
print_info_video_in_playlist() - Вывод информации о нахождении видео в плейлисте

Методы класса:
get_playlist(playlist_id) - Получает данные о плейлисте
get_playlist_channel(channel_id) - Получает плейлист канала
