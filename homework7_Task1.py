line = "пара-ра-рам рам-пам-папам па-ра-па-да"
lines = line.split()
print(lines)
lst = [sum(x in 'уеыаоэяию' for x in lines)]

for lin in lines:
    if len(set(lst)) == 1 :
        res = "Парам пам-пам"  
    else: res = "Пам парам"
print(res)