# Задача 1
# Вы собрали своего робота, который может писать любые программы. Его первая программа выглядит так:

n = int(input())
a = [0]
for i in range(n):
    x = int(input())
    a = [i] * x
print(a)

# В ответе напишите, что будет выведено при последовательном вводе чисел: 3, 5, 4, 3.
# Ответ: [2, 2, 2]. На самой последней иттерации создается массив из илемента "2" и умножается на последний
# введенный x. И получается массив размера x, состоящий их одинаковых ээлементов i (i в конце равно n-1).

# Задача 2
# Ваш робот написал еще одну программу:

n = int(input())
a = []
for i in range(n):
    a = a + [i] * i
print(a)

# Что будет выведено в результате работы программы при вводе числа 3?
# Ответ: [1, 2, 2]. Создаются массивы из 0 по 0 элементов, из 1 по 1 эл-ту, из 2 по 2 эл-та и тд..

# Задача 3
# На вход подается число n, затем последовательность из n чисел. Создайте массив, состоящий из чисел этой
# последовательности. В ответ запишите среднее арифмети- ческое всех элементов массива для n = 5 и последовательности
# [2, 3, 1, 5, 10]

n = int(input())
a = [0]*n
sum=0
for i in range(n):
    a[i] = int(input()) # ввод с клавиатуры значения массива
    sum+=a[i] # сразу же считаем сумму всех элементов
mid = sum/n
print(mid)

# ответ: 4.2

# Задача 4
# На вход последовательно подаются числа n и m, затем последовательность из n чисел. Создайте массив,
# состоящий из чисел этой последовательности. Напишите программу, которая выводит элемент с индексом m.
# В ответе укажите результат работы программы для следующей последовательности:
# 10, 3, 1, 10, 23, 32, 18, 74, 29, 73, 1, 82

# ЛеНЬ делать

# Задача 5
# На вход подается число n, затем последовательность из n чисел. Создайте массив, состоящий из чисел этой
# последовательности. В ответ запишите сумму чисел массива с шагом два, начиная с 0 элемента. В ответе запишите
# результат работы программы для последовательности 6, 1, 9, 2, 8, 3, 7

n = int(input())
a = [0]*n
sum=0
for i in range(n):
    a[i] = int(input())
for i in range(0,n,2):
    sum+=a[i]
print(sum)

# ответ:6