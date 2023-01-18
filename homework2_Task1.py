n = int(input('введите количество монет  '))
sum1 = 0
sum2 = 0
for i in range(n):
    x = int(input('введите сторону монеты 0 или 1  '))
    if x == 0:
        sum1 = sum1 + 1
    else:
        sum2 = sum2 + 1
if sum1<sum2:
    print(sum1)
else:
    print(sum2)