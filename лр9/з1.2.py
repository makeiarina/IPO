import math #Импортируем модуль math для использования математических функций

def distance(point1, point2):#Определяем функцию distance, которая принимает две точки point1 и point2 в формате (x, y)
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)#Вычисляем расстояние между двумя точками по формуле sqrt((x2 - x1)^2 + (y2 - y1)^2) и возвращаем результат.


def find_max_distance(points):#Определяем функцию find_max_distance, которая принимает список точек points
    # Инициализируем переменные max_distance и max_points для хранения максимального расстояния и соответствующих точек
    max_distance = 0
    max_points = []

    for i in range(len(points)):# Итерируемся по индексам точек с помощью циклов for
        for j in range(i+1, len(points)):#Внутри вложенного цикла for вычисляем расстояние между текущими точками и проверяем, является ли оно больше текущего максимального расстояния
            dist = distance(points[i], points[j])
            if dist > max_distance:#Если расстояние больше текущего максимального, обновляем max_distance и max_points, присваивая им текущие точки в виде списка с одним элементом
                max_distance = dist
                max_points = [(points[i], points[j])]
            elif dist == max_distance:#Если расстояние равно текущему максимальному, добавляем текущие точки в max_points
                max_points.append((points[i], points[j]))

    return max_distance, max_points

# Точки заданы координатами (x1, y1), (x2, y2), (x3, y3), (x4, y4)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]#Задаем список точек points с координатами (x1, y1), (x2, y2), (x3, y3), (x4, y4)

max_distance, max_points = find_max_distance(points)# Вызываем функцию find_max_distance и сохраняем результаты в переменные max_distance и max_points

print("Максимальное расстояние:", max_distance)
print("Точки, находящиеся на максимальном расстоянии:")

for point_pair in max_points:#Выводим максимальное расстояние и точки, находящиеся на этом расстоянии, с помощью цикла for
    print(point_pair)