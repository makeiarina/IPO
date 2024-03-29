import numpy as np  # Импорт библиотеки NumPy с псевдонимом np

def calculate_sum_and_positive_count(arr):  # Определение функции для вычисления суммы элементов и количества положительных элементов в массиве
    arr = np.array(arr)  # Преобразование входного списка в массив NumPy
    sum_of_elements = np.sum(arr)  # Вычисление суммы всех элементов массива
    positive_count = np.sum(arr > 0)  # Подсчет количества положительных элементов в массиве
    return sum_of_elements, positive_count  # Возврат кортежа из суммы элементов и количества положительных элементов

# Пример использования функции
my_array = [1, -2, 3, -4, 5]  # Заданный массив
result = calculate_sum_and_positive_count(my_array)  # Вызов функции для получения результатов
print("Сумма элементов массива:", result[0])  # Вывод суммы элементов массива
print("Количество положительных элементов:", result[1])  # Вывод количества положительных элементов в массиве
