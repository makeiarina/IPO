import numpy as np# Импорт библиотеки NumPy под псевдонимом np

def calculate_determinant(matrix):
    determinant = np.linalg.det(matrix)# Вычисление определителя матрицы с использованием функции det из библиотеки NumPy
    return determinant# Возвращение значения определителя

def solve_linear_equation(matrix_A, vector_b):
    solution = np.linalg.solve(matrix_A, vector_b)# Решение системы линейных уравнений Ax=b с использованием функции solve из библиотеки NumPy
    return solution # Возвращение решения системы уравнений

matrix_A = np.array([[2, 1], [1, 1]])# Создание двумерного массива - матрицы A
vector_b = np.array([3, 2])# Создание одномерного массива - вектора b

# Вычисление определителя матрицы
determinant = calculate_determinant(matrix_A)# Вызов функции calculate_determinant для вычисления определителя матрицы A
print("Определитель матрицы A:")
print(determinant)# Вывод значения определителя матрицы A

# Решение системы уравнений
solution = solve_linear_equation(matrix_A, vector_b)# Вызов функции solve_linear_equation для решения системы уравнений
print("\nРешение системы уравнений:")
print(solution)# Вывод решения системы уравнений
