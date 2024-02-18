import requests
import json  # Импорт библиотеки для работы с JSON

result = requests.get("https://swapi.dev/api/people/3/")  # Отправка GET-запроса по указанному URL
if result.status_code == 200:
    json_dict = json.loads(result.text)  # Десериализация JSON-строки в словарь
    json_dict['name'] = input("Введите имя: ")
    with open("swap.json", "w") as file:  # Открытие файла swap.json для записи
        json_text = json.dump(json_dict, file, indent=4)  # Сериализация словаря в JSON и запись в файл с отступом 4
    # Дополнительный код:
    result_homeworld = requests.get(json_dict['homeworld'])  # Отправка запроса по URL из поля homeworld
    print(result_homeworld.text)  # Вывод информации о месте происхождения героя
