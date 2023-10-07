numbers = []#Создаем пустой список numbers
n = int(input("Введите количество элементов в массиве: "))#Вводим количество элементов в массиве и преобразуем его в целое число с помощью int()

for i in range(n):#Запускаем цикл for для n итераций
    num = int(input(f"Введите число {i+1}: "))#Вводим число и преобразуем его в целое число с помощью int()
    numbers.append(num)#Добавляем полученное число в список numbers с помощью метода append()

max_val = max(numbers)# Находим максимальный элементы
min_val = min(numbers)# Находим минимальный элементы

max_index = numbers.index(max_val)#Находим индекс максимального элемента с помощью метода index()
min_index = numbers.index(min_val)#Находим индекс минимального элемента с помощью метода index()

numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]# Меняем максимальный и минимальный элементы местами

print("Измененный массив:", numbers)# Отображение измененного массива