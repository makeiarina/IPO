import my_module1

m = int(input("Введите M: "))
n = int(input("Введите N: "))
print(f"Число из интервала [{m}, {n}], имеющее наибольшее количество делителей: {my_module1.max(m, n)}")