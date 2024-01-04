import urllib.parse
url = 'https://oaek.by/'
parsed_url = urllib.parse.urlparse(url)
print(parsed_url)
#1. scheme: Схема URL (например, ‘http’ или ‘https’). В нашем случае это ‘https’.
#2. netloc: Сетевое местоположение, обычно включает имя хоста и порт. В нашем случае это ‘news.yandex.ru’.
#3. path: Путь к ресурсу на сервере. В нашем случае это ‘/story/Название_новости’.
#4. params: Параметры для работы с ресурсом. В нашем случае это пустая строка, так как параметры отсутствуют.
#5. query: Строка запроса, которая может содержать дополнительную информацию, передаваемую серверу. В нашем случае это пустая строка, так как строка запроса отсутствует.
#6. fragment: Фрагмент URL, который обычно используется для навигации по странице. В нашем случае это пустая строка, так как фрагмент отсутствует.
import urllib.parse
# Предположим, что parsed_url - это ваш разобранный URL
reconstructed_url = urllib.parse.urlunparse(parsed_url)
print(reconstructed_url)
import urllib.parse
# Предположим, что parsed_url - это ваш разобранный URL
reconstructed_url = urllib.parse.urlunparse(parsed_url)
print(reconstructed_url)