# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_elem = int(input('Введите минимальный элемент: '))
max_elem = int(input('Введите максимальный элемент: '))
list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
def index(list):
    for i in range(len(list)):
        if min_elem <= list[i] <= max_elem:
            print(i, end = ' ')
index(list)