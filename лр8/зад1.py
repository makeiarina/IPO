n=int(input("Введите число: "))#В этой строке мы просим пользователя ввести целое число и сохраняем его в переменной `n`.
prost=list(range(n+1))# Создать список чисел от 0 до введенного числа n
prost[1]=0# Установить значение первого элемента списка (числа 1) на 0, так как 1 не является простым числом
for i in range(n+1):# Проходим по всем числам в списке
        if prost[i]!=0:
            for j in range(i+i,n+1,i):
                prost[j]=0
prost = set(prost)  # Преобразование списка в множество
prost.remove(0)  # Удаление нуля из множества

print(prost)  # Вывод множества простых чисел