class Student:# определяется класс Student. У класса есть три атрибута: name, group и marks, которые инициализируются при создании нового экземпляра класса
    def __init__(self, name, group, marks):
        self.name=name
        self.group=group
        self.marks=marks
students=[]#Здесь создается список students из 5 экземпляров класса Student, которые заполняются с клавиатуры
for i in range(5):
    name=input("Введите фамилию и инициалы студента: ")
    group=input("Введите номер группы студента: ")
    marks=[]
    for i in range(5):
        mark=int(input(f"Введите успеваемость (отметка {i + 1}): "))
        marks.append(mark)
    student=Student(name, group, marks)
    students.append(student)
students_with_low_marks=[]#поиск студентов с оценками ниже 4 и добавление их в список students_with_low_marks.
for student in students:
    has_low_mark=False
    for mark in student.marks:
        if mark<4:
            has_low_mark=True
            break
    if has_low_mark:
        students_with_low_marks.append(student)
if len(students_with_low_marks)>0:#вывод информации о студентах с оценками ниже 4 и вывод сообщения, если таких студентов не найдено.
    print("Студенты с неудовлетворительными отметками:")
    for student in students_with_low_marks:
        print(f"Фамилия и инициалы: {student.name} номер группы: {student.group}")
else:
    print("Нет студентов с неудовлетворительными отметками")