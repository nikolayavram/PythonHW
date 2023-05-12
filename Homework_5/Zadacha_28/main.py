# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.



def sum(a, b):
    if b <= 0:
        return a + 0

    return sum(a + 1, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
print(f"Сумма равна: {sum(a, b)}")