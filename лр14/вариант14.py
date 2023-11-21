class Department:
    def __init__(self, room, building, contact_phone, head_surname, num_teachers):
        self.room = room
        self.building = building
        self.contact_phone = contact_phone
        self.head_surname = head_surname
        self.num_teachers = num_teachers
#Создается класс "Department", который представляет отделение. У него есть конструктор __init__, который принимает аргументы room, building, contact_phone, head_surname и num_teachers.
# Значения этих аргументов присваиваются соответствующим атрибутам объекта
class StudentGroup(Department):
    def __init__(self, room, building, contact_phone, head_surname, num_teachers, group_name, admission_year, specialty):
        super().__init__(room, building, contact_phone, head_surname, num_teachers)
        self.group_name = group_name
        self.admission_year = admission_year
        self.specialty = specialty
#Создается класс "StudentGroup", который наследуется от класса "Department". У него также есть конструктор __init__, который принимает все аргументы конструктора класса "Department", а также аргументы group_name, admission_year и specialty.
# С помощью ключевого слова super() вызывается конструктор класса "Department" для инициализации атрибутов, наследуемых от него.
# Затем задаются атрибуты group_name, admission_year и specialty
class Student(Department):
    def __init__(self, room, building, contact_phone, head_surname, num_teachers, department, group, full_name, gender, address):
        super().__init__(room, building, contact_phone, head_surname, num_teachers)
        self.department = department
        self.group = group
        self.full_name = full_name
        self.gender = gender
        self.address = address
# Создается класс "Student", также наследующий от класса "Department". Он имеет конструктор __init__, который принимает все аргументы конструктора класса "Department", а также аргументы department, group, full_name, gender и address.
# С помощью super() вызывается конструктор класса "Department".
# Затем задаются атрибуты department, group, full_name, gender и address
class DepartmentTeacher(Department):
    def __init__(self, room, building, contact_phone, head_surname, num_teachers, department, full_name, position, experience, disciplines):
        super().__init__(room, building, contact_phone, head_surname, num_teachers)
        self.department = department
        self.full_name = full_name
        self.position = position
        self.experience = experience
        self.disciplines = disciplines
#Создается класс "DepartmentTeacher", также наследующий от класса "Department". У него есть конструктор __init__, который принимает все аргументы конструктора класса "Department", а также аргументы department, full_name, position, experience и disciplines.
# С помощью super() вызывается конструктор класса "Department".
# Затем задаются атрибуты department, full_name, position, experience и disciplines
# Создание объекта отделения
department = Department("103", "Корпус А", "+7-123-456-7890", "Иванов", 6)
# Создание объекта студенческой группы
group = StudentGroup("103", "Корпус А", "+7-123-456-7890", "Иванов", 6, "Группа 1", 2022, "Информатика")
# Создание объекта студента
student = Student("103", "Корпус А", "+7-123-456-7890", "Иванов", 6, department, group, "Иванов Иван Иванович", "Мужской", "г. Москва, ул. Пушкина, д. 10")
# Создание объекта преподавателя отделения
teacher = DepartmentTeacher("103", "Корпус А", "+7-123-456-7890", "Иванов", 6, department, "Петров Петр Петрович", "Преподаватель", 10, ["Математика", "Физика"])
# Вывод информации об отделении
print("Информация об отделении:")
print("Аудитория:", department.room)
print("Корпус:", department.building)
print("Контактный телефон:", department.contact_phone)
print("Фамилия заведующего:", department.head_surname)
print("Количество преподавателей:", department.num_teachers)
# Вывод информации о студенческой группе
print("\nИнформация о студенческой группе:")
print("Аудитория:", group.room)
print("Корпус:", group.building)
print("Контактный телефон:", group.contact_phone)
print("Фамилия заведующего:", group.head_surname)
print("Количество преподавателей:", group.num_teachers)
print("Название группы:", group.group_name)
print("Год поступления:", group.admission_year)
print("Специальность:", group.specialty)
# Вывод информации о студенте
print("\nИнформация о студенте:")
print("Аудитория:", student.room)
print("Корпус:", student.building)
print("Контактный телефон:", student.contact_phone)
print("Фамилия заведующего:", student.head_surname)
print("Количество преподавателей:", student.num_teachers)
print("Отделение:", student.department)
print("Группа:", student.group.group_name)
print("ФИО студента:", student.full_name)
print("Пол:", student.gender)
print("Адрес:", student.address)
# Вывод информации о преподавателе
print("\nИнформация о преподавателе:")
print("Аудитория:", teacher.room)
print("Корпус:", teacher.building)
print("Контактный телефон:", teacher.contact_phone)
print("Фамилия заведующего:", teacher.head_surname)
print("Количество преподавателей:", teacher.num_teachers)
print("Отделение:", teacher.department)
print("ФИО преподавателя:", teacher.full_name)
print("Должность:", teacher.position)
print("Стаж:", teacher.experience)
print("Дисциплины:", teacher.disciplines)