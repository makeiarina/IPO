import requests  # Импорт библиотеки для выполнения HTTP-запросов
import json  # Импорт библиотеки для работы с JSON

result = requests.get("https://swapi.dev/api/films/1/")  # Выполнение GET-запроса по указанному URL и сохранение результата
json_dict = json.loads(result.text)  #Функция loads() модуля json преобразует строку в формате JSON в объект Python.
print(json_dict["opening_crawl"])  # Вывод на экран значения по ключу "opening_crawl" из полученного JSON-словаря