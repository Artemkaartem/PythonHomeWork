# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input("Введите целое число: "))
st = 1
while 2 ** st <= n:
    print(2 ** st, end=' ')
    st += 1