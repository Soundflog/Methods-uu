i_str = str(input("Введите строку:")).lower()


def quest_1(i):
    list(i).sort()
    result = ['']
    for x in sorted(list(i)):
        result.append(x)
    print("".join(result))


quest_1(i_str)
i_fibonacci = int(input("Введите число n для вычисление n-го числа ряда Фибоначчи:"))


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(i_fibonacci))

i_multiplication = input("Введите 2 целых числа через пробел: ")
i_quest = int(input("Какой будет результат? -->"))


def table_multiplication(number, quest):
    result = int(number[0]) * int(number[1])
    if result == int(quest):
        print("Верно")
    else:
        print("Ошибка, верный ответ =", result)


table_multiplication(i_multiplication.split(), int(i_quest))
