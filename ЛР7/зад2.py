pr={'Чай':10.99, 'Какао':12.99, 'Кофе':14.99,'Лимон': 5.00, 'Кефир': 1.99, 'Сахар':2.46, 'Соль':0.61, 'Молоко':2.48}#создаем словарь
for key, value in pr.items():#Начало цикла
    print(key, ":", value)# Выводим список продуктов и их цен
key = input("Введите ключ: ")# Запрашиваем у пользователя ключ (название продукта)
value = pr.get(key)# Используем метод get, чтобы получить значение (цену) продукта по введенному ключу
print("Цена продукта", key, ":", value)# Выводим цену продукта