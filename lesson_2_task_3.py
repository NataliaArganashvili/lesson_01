import math

def square(a):
    return math.ceil(a*a)

a = float(input("Введите длину сторона квадрата: "))
print(f"Округленная в большую сторону сумма - {square(a)}")
