# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

n = int(input("Введите длину массива: "))  
a = []

for i in range(n):
    a.append(int(input(f"Введите элемент {i}: ")))
print(a)

x = int(input("Число: ")) 
count = 0

for i in range(n): 
    if a[i] == x:  
        count += 1

print(count)
