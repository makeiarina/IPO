import numpy as np  # Импорт библиотеки NumPy под псевдонимом np

# Генерация случайного числа для числа строк в диапазоне от 15 до 100
rows = np.random.randint(15, 101)
# Генерация случайного числа для числа столбцов в диапазоне от 15 до 100
cols = np.random.randint(15, 101)

# Создание случайной матрицы размером (rows, cols) с элементами от 1 до 1000
matrix = np.random.randint(1, 1001, size=(rows, cols))
print('Исходная матрица:')
print(matrix)

# Нахождение максимального элемента в строке 14
max_element_row14 = np.max(matrix[14, :])
print(f'Максимальный элемент в строке 14: {max_element_row14}')

# Умножение всех элементов матрицы на максимальное значение из строки 14
matrix_multiplied = matrix * max_element_row14
print('Матрица, умноженная на максимальный элемент строки 14:')
print(matrix_multiplied)

