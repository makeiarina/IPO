import numpy as np# Импорт библиотеки NumPy под псевдонимом np

# Создание массива 3x4 из случайных чисел с нормальным распределением
mean = 0# Среднее значение для нормального распределения
std_dev = 1.0# Стандартное отклонение для нормального распределения
array_3x4 = np.random.normal(mean, std_dev, (3, 4))# Создание двумерного массива 3x4 из чисел с нормальным распределением
print("Массив 3x4 из нормального распределения:")
print(array_3x4)# Вывод созданного массива 3x4

# Преобразование массива 3x4 в одномерный массив
array_1d = array_3x4.flatten()# Преобразование двумерного массива 3x4 в одномерный массив
print("\nОдномерный массив с таким же size:")
print(array_1d)# Вывод одномерного массива с теми же элементами, что и в исходном двумерном массиве