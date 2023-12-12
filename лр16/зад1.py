class Computer:#  Эта строка определяет новый класс с именем "Computer".
    def __init__(self, brand, model, processor, ram, storage):# Это конструктор метод __init__ для класса Computer. Он инициализирует атрибуты объекта brand, model, processor, ram и storage значениями, переданными при создании экземпляра.
        #  Эти строки присваивают значения, переданные в конструктор, атрибутам объекта.
        self._brand = brand
        self._model = model
        self._processor = processor
        self._ram = ram
        self._storage = storage
## Каждое свойство определено с использованием декоратора @property, который позволяет получать доступ к значениям этих свойств и задавать новые значения с помощью сеттеров
    @property
    def brand(self):#  Эта строка определяет свойство под названием brand, которое позволяет нам получить значение _brand с использованием точечной нотации.
        return self._brand#Эта строка возвращает значение атрибута _brand, когда свойство brand запрашивается.

    @brand.setter
    def brand(self, value):#Эта строка определяет метод-сеттер для свойства brand, который позволяет устанавливать значение _brand с использованием точечной нотации.
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, value):
        self._processor = value

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        self._ram = value

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value

my_computer = Computer('Lenovo', 'ideapadGAMING3', 'Intel Core i5', 8, 512)## Создание экземпляра объекта класса Computer
print(my_computer.brand)  # Lenovo
print(my_computer.model)  # ideapadGAMING3
print(my_computer.processor)  # Intel Core i5
print(my_computer.ram)  # 8
print(my_computer.storage)  # 512
my_computer.brand = 'HP'
my_computer.model = 'Pavilion 14'
my_computer.processor = 'AMD Ryzen 7'
my_computer.ram = 16
my_computer.storage = 1024
print(my_computer.brand)  # HP
print(my_computer.model)  # Pavilion 14
print(my_computer.processor)  # AMD Ryzen 7
print(my_computer.ram)  # 16
print(my_computer.storage)  # 1024
