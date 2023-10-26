with open(f"file1_{14}.txt", "r") as file1, open(f"file2_{14}.txt", "w") as file2:
    numbers = [int(line) for line in file1]
    if len(numbers) % 2 != 0:
        print("Количество введенных чисел должно быть четным")
        exit()

    for i in range(0, len(numbers), 2):
        sum_of_nums = numbers[i] + numbers[i + 1]
        file2.write(str(sum_of_nums) + "\n")
    print('Сумма записана в текстовый файл file2_14.txt')