with open(f"file1_{14}.txt", "r") as file1, open(f"file2_{14}.txt", "w") as file2:# Открываем файл file1_NN.txt для чтения и file2_NN.txt для записи
    numbers = [int(line) for line in file1]# Читаем все числа из file1_NN.txt и сохраняем их в список numbers
    if len(numbers) % 2 != 0:# Проверяем, что количество чисел в списке numbers четное
        print("Количество введенных чисел должно быть четным")
        exit()

    for i in range(0, len(numbers), 2):  # Проходим по списку numbers с шагом 2
        sum_of_nums = numbers[i] + numbers[i + 1] # Вычисляем сумму пары чисел
        file2.write(str(sum_of_nums) + "\n") # Записываем сумму в file2_NN.txt
    print('Сумма записана в текстовый файл file2_14.txt')# Выводим сообщение о успешной записи суммы в файл