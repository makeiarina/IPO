def num(n):#Определяем функцию num(n), которая считает количество делителей числа n
    c = 0#Инициализируем счетчик c равным нулю
    for number in range(1, n + 1):#Используя цикл for, проходимся по числам от 1 до n+1
        if n % number == 0:#Если число n делится на number без остатка (n % number == 0), увеличиваем счетчик c на 1
            c += 1
    return c#Возвращаем значение счетчика c

def max(m, n):
    max = 0
    max = m
    for number in range(m, n + 1):
        dam = num(number)
        if dam > max:
            max = dam
            max = number
    return max

m = int(input("Введите M: "))
n = int(input("Введите N: "))
print(f"Число из интервала [{m}, {n}], имеющее наибольшее количество делителей: {max(m, n)}")