# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества  '))
A = set([int(input()) for i in range(n)])
print(A)

m = int(input('Введите количество элементов второго множества  '))
B = set([int(input()) for i in range(m)])
print(B)
my_set = A.intersection(B)
res = list(my_set)
print(sorted(res))