# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

A = int(input("Введите число A:"))
B = int(input("Введите число B:"))     

def Number(A,B):
    if B == 0:
        return 1
    return A**B
print(Number(A,B))