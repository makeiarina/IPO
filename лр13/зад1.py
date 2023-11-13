import math#Импортируем модуль math
class Drob:#Создаем класс дробь
    def __init__(self, m, n):#Задаем аргументы с помощью конструктора
        self.m=m#Присваиваем каждому аргументу переменную
        self.n=n
        self.normalize()#Сокращение дроби
    def __str__(self):
        return f'{self.m}/{self.n}'#Выводим дробь
    def __add__(self, other):#Метод сложения
        m1=self.m*other.n+other.m*self.n#Складываем дроби
        n1=self.n*other.n#Приводим к общему знаменателю
        return Drob(m1, n1)#Возвращаем полученную дробь
    def __sub__(self, other):#Метод вычитания
        m2=self.m*other.n-other.m*self.n#Вычитаем дроби
        n2=self.n*other.n#Приводим к общему знаменателю
        return Drob(m2, n2)#Возвращаем полученную дробь
    def __mul__(self, other):#Метод умножения
        m3=self.m*other.m#Умножаем числители дробей
        n3=self.n*other.n#Умножаем знаменатели дробей
        return Drob(m3, n3)#Возвращаем полученную дробь
    def __truediv__(self, other):#Метод деления
        m4=self.m*other.n#Умножаем числитель одной дроби на знаменатель другой
        n4=self.n*other.m#Умножаем знаменатель одной дроби на числитель другой
        return Drob(m4, n4)#Возвращаем полученную дробь
    def normalize(self):#Метод для сокращения дробей
        c=math.gcd(self.m, self.n)#Числитель и знаменатель
        self.m=self.m//c
        self.n=self.n//c
    def __eq__(self, other):#Метод для проверки равенства
        return self.m*other.n==other.m*self.n#Возвращаем дробь
    def __lt__(self, other):#Метод для сравнения дробей
        return self.m*other.n<self.n*other.m
d1=Drob(4, 3)#Значения числителей и знаменателей дробей
d2=Drob(6, 5)#Значения числителей и знаменателей дробей
print(f'{d1}+{d2}={d1+d2}')#Выводим сумму
print(f'{d1}-{d2}={d1-d2}')#Выводим разность
print(f'{d1}*{d2}={d1*d2}')#Выводим произведение
print(f'{d1}/{d2}={d1/d2}')#Выводим частное
print(f'{d1}=={d2}:{d1==d2}')#Выводим правду или ложь
print(f'{d1}<{d2}:{d1<d2}')#Выводим правду или ложь
d5=Drob(2, 12)
print(d5)#Выводим сокращенную дробь