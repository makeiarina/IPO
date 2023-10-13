sequence = input("Введите последовательность символов: ")#мы запрашиваем у пользователя ввод последовательности символов с помощью функции `input()`. Введенная последовательность будет сохранена в переменной `sequence`.
seet = set()#Здесь мы создаем пустое множество с помощью функции set()
for c in sequence:#Эта строка кода запускает цикл for, который будет проходить через каждый символ в переменной `sequence`
    if c.isdigit() and int(c) % 2 != 0:# В этой строке кода мы проверяем, является ли текущий символ числом и нечетным
        seet.add(c)#В данной строке кода мы добавляем текущий символ в множество seet с помощью метода add()
    elif c== 'Z':#Здесь мы проверяем, равен ли текущий символ Z. Если это так, то мы добавляем символ `'Z'` в множество seet.
        seet.add(c)

print("Множество элементов:", seet) #В этой строке кода мы выводим на экран строку "Множество элементов:" и содержимое множества