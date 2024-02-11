import requests#Этот оператор импортирует модуль requests, который используется для отправки HTTP-запросов.
from bs4 import BeautifulSoup#Эта строка импортирует класс BeautifulSoup из модуля bs4, который используется для парсинга HTML и XML.
import csv#Этот оператор импортирует модуль csv, который позволяет работать с файлами CSV.
url = " https://www.sber-bank.by/"#Эта строка устанавливает URL-адрес веб-сайта, с которого будет получена информация.
r = requests.get(url)# Этот запрос отправляет HTTP GET-запрос по указанному URL-адресу и сохраняет ответ в переменной r
print(r)#Этот оператор выводит HTTP-код ответа на запрос
soup = BeautifulSoup(r.text,"html.parser")#Здесь используется BeautifulSoup для парсинга HTML-кода ответа и создания объекта soup, представляющего структуру страницы
print(soup)#Этот оператор выводит содержимое объекта soup
items = soup.find_all("tr")#Здесь мы ищем все теги <tr> на странице
print(items)
curr = []#Эта строка создает пустой список curr

with open('curr_bank.csv',"w") as file:#Здесь открывается файл с именем "curr_bank.csv" для записи
    writer = csv.DictWriter(
    file,
    fieldnames = ['Валюта','Покупка','Продажа'],
    delimiter = ';',
    lineterminator = '\r',
    quoting = csv.QUOTE_MINIMAL
    )#Создается объект writer, который используется для записи словарей в CSV-файл.
    writer.writeheader()#Этот оператор записывает заголовок в CSV-файл.
    for elem in curr:#Здесь происходит запись данных из списка curr в CSV-файл.
        writer.writerow(elem)
print('Запись окончена')#Этот оператор выводит сообщение о завершении записи.