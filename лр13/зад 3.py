class Rub: #определяет класс Rub для работы с суммами денег в рублях и копейках
    def __init__(self, rub=0, kop=0):#Метод инициализации класса, устанавливает атрибуты rub и kop.
        self.rub = rub
        self.kop = kop
        self.normalize()#Вызывает метод normalize() для нормализации значений.
    def normalize(self):# Метод нормализации суммы, переводит копейки в рубли, если количество копеек больше либо равно 100.
        self.rub += self.kop // 100
        self.kop = self.kop % 100
    def __str__(self):#Метод форматирования суммы для вывода.
        return f"{self.rub}.{self.kop:02d}"
    def __lt__(self, other):#Метод сравнения для операции "<", сравнивает два объекта класса Rub.
        if self.rub < other.rub: #Проверяет условие, если значение rub текущего объекта меньше другого, возвращает True.
            return True
        elif self.rub == other.rub and self.kop < other.kop:#Если rub равны, то сравнивает значения kop.
            return True
        return False#Если ни одно из условий не выполняется, возвращает False.
    def __add__(self, other): #Метод для сложения двух объектов класса Rub.
        res = Rub(self.rub + other.rub, self.kop + other.kop) #Создает новый объект Rub и заполняет его значениями суммы текущего объекта и другого.
        res.normalize()#Нормализует сумму и возвращает ее.
        return res
    def __sub__(self, other): #Метод вычитания, вычитает один объект Rub из другого.
        res = Rub(self.rub - other.rub, self.kop - other.kop)#Создает новый объект Rub и заполняет его значениями разности текущего объекта и другого.
        res.normalize()#Нормализует сумму и возвращает ее.
        return res
class Food:#определяет класс Food, представляющий продукт.
    def __init__(self, name='', rub=0, kop=0):#Метод инициализации класса, устанавливает атрибуты name и price.
        self.name = name#Устанавливает атрибут имени продукта.
        self.price = Rub(rub, kop) #Создает объект Rub для хранения цены продукта.
products = ["rice 8.59", "tea 4.99", "cake 24.56", "salad 5.69"]#Список продуктов с указанием названия и цены.
food = []
total_price = Rub()
for line in products:# Цикл для обработки каждой строки в списке продуктов.
    name, price_str = line.split()#Разделяет строку на название продукта и строку цены.
    rub, kop = map(int, price_str.split('.'))#Разделяет цену на рубли и копейки. Преобразует их в целые числа.
    food.append(Food(name, rub, kop))#Создает объект Food и добавляет его в список продуктов.
    total_price += Rub(rub, kop)#Добавляет цену текущего продукта к общей сумме.
food.sort(key=lambda x: x.price, reverse=True)#Сортирует список продуктов по цене в обратном порядке.
print("Список продуктов:")#Выводит заголовок для списка продуктов.
for product in food:#Выводит каждый продукт и его цену.
    print(product.name, product.price)
print('-----')#Выводит разделительную строку.
print(f"Итоговая сумма: {total_price} руб")#Выводит итоговую сумму всех продуктов.
customer_rub = int(input("Введите количество рублей, которые дал покупатель: "))#Получает количество рублей, которые дал покупатель.
customer_kop = int(input("Введите количество копеек, которые дал покупатель: "))#Получает количество копеек, которые дал покупатель.
customer_payment = Rub(customer_rub, customer_kop)#Создает объект Rub для хранения суммы, которую дал покупатель.
change = customer_payment - total_price#Вычисляет и выводит сумму сдачи, вычитая общую сумму от суммы, которую дал покупатель.
print(f"Сдача составляет: {change}")