class Rub:#Создаем класс
    def __init__(self, rub=0, kop=0):#Задаем аргументы через конструктор
        self.rub=rub
        self.kop=kop
        self.normalize()
    def normalize(self):#Создаем класс для подсчета
        self.rub+=self.kop//100
        self.kop=self.kop%100
    def __str__(self):#Создаем класс который выводит правильное написание
        return f"{self.rub}.{self.kop}"
    def __lt__(self, other):#Класс для сравнения
        if self.rub<other.rub:
            return True#Возвращаем правду, если условие истино
        elif self.rub==other.rub and self.kop<other.kop:#Иначе(если выполняются другие условия)
            return True#Возвращаем правду
        return False
    def __add__(self, other):#Класс для сложения
        res=Rub(self.rub+other.rub, self.kop+other.kop)
        res.normalize()
        return res
class Food:#Создаем класс
    def __init__(self, name='', rub=0, kop=0):#С помощью конструктора задаем аргументы
        self.name=name
        self.price=Rub(rub, kop)
products=["rice 8.59", "tea 4.99", "cake 24.56", "salad 5.69"]#Выводим цены и продекты
food=[]
total_price=Rub()
for line in products:#Перебираем каждую строку в продуктах
    name, price_str=line.split()
    rub, kop=map(int, price_str.split('.'))#Функция map () используется для применения функции к каждому элементу
    food.append(Food(name, rub, kop))
    total_price+=Rub(rub, kop)
food.sort(key=lambda x: x.price, reverse=True)
for product in food:#Перебираем каждый продукт с ценой и выводим его на экран
    print(product.name, product.price)
print('-----')
print(f"total {total_price} rub")