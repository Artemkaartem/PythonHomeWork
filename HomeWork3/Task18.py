# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input('Введите количество элементов: '))
element = input("Введите через пробел элементы списка: ").split()
spisok = list(map(int, element))
if len(spisok) != N or N == 0:
    print('Не правильно введено количество элементов')
else:
    X = int(input('Введите число X: '))
    min = X - spisok[0]
    index = 0
    for i in range(1, N):
        count = abs(X - spisok[i])
        if count < min:
            min = count
            index = i
    print(f'Число {spisok[index]} самый близкий по величине элемент к заданному числу {X}')