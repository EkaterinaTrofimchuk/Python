# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X


count=0
list1 = []
x= int(input('введите число Х  '))
n = int(input('введите число N  '))
for i in range(1,n+1):
    list1.append(i)
print(list1)

for i in range(1, len(list1)):
    if list1[i]==x:
        count=count+1
print(count)