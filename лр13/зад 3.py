class Rub:
    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop
        self.normalize()
    def normalize(self):
        self.rub += self.kop // 100
        self.kop = self.kop % 100
    def __str__(self):
        return f"{self.rub}.{self.kop:02d}"
    def __lt__(self, other):
        if self.rub < other.rub:
            return True
        elif self.rub == other.rub and self.kop < other.kop:
            return True
        return False
    def __add__(self, other):
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res
    def __sub__(self, other):
        res = Rub(self.rub - other.rub, self.kop - other.kop)
        res.normalize()
        return res
class Food:
    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)
products = ["rice 8.59", "tea 4.99", "cake 24.56", "salad 5.69"]
food = []
total_price = Rub()
for line in products:
    name, price_str = line.split()
    rub, kop = map(int, price_str.split('.'))
    food.append(Food(name, rub, kop))
    total_price += Rub(rub, kop)
food.sort(key=lambda x: x.price, reverse=True)
print("Список продуктов:")
for product in food:
    print(product.name, product.price)
print('-----')
print(f"Итоговая сумма: {total_price} руб")
customer_rub = int(input("Введите количество рублей, которые дал покупатель: "))
customer_kop = int(input("Введите количество копеек, которые дал покупатель: "))
customer_payment = Rub(customer_rub, customer_kop)
change = customer_payment - total_price
print(f"Сдача составляет: {change}")