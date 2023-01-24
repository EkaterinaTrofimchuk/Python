list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minV = int(input('Введите минимум '))
maxV = int(input('Введите максимум '))
list2 = []
for i in range(len(list1)):
    if list1[i]>minV and list1[i]<maxV:
        list2.append(list1[i])
print(list2)
