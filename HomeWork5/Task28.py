# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Введите число A:"))
b = int(input("Введите число B:"))     

def sum(a, b):
    if a < 0 or b < 0:       
        return print('Неверный ввод') 
    return a + b 
print(sum(a, b))