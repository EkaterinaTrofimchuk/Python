# Написать программу, которая проверяет счастливость билета

s=input('Введите шестизначный номер билета')
a = int(s[0]) + int(s[1]) + int(s[2])
b = int(s[3]) + int(s[4]) + int(s[5])
if a == b:
    print('Билет счастливый')
else:
    print('Билет не счастливый')