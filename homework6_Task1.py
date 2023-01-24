a0 = int(input('Введите первое число: '))
d = int(input('Введите разность '))
n = int(input('Введите количество n '))



def progr(a0,d,n):
    for i in range (n):
        if n==1:
            print (a0)
        else:
            print (a0+d*i)
    return

progr(a0,d,n)