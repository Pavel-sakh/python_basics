"""
4. Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(x,y):
    my_num = x
    for i in range(-y - 1):
        my_num *= x
    return 1 / my_num


x = int(input("Введите действительное положительное число х: "))
y = int(input("Введите целое отрицательное число y: "))
print(f"Возводим число {x} в степень {y}, равно = {my_func(x, y)}")
