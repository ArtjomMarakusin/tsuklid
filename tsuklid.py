## Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n елок. Изображение одной елки имеет размер 4×9 символов, между двумя соседними елками также имеется пустой (из пробелов) столбец. 
# Разрешается вывести пустой столбец после последней елки. Для упрощения рисования скопируйте елку из примера в среду разработки. Елки должны простоложиться горизонтально.

print("1.")

elka = ['   /V\    ',
       '  / V \   ',
       ' / V V \  ',
       '/VV V VV\ ',
       ]
n = 6
 
for i in elka:
    print(i * n)

##---------------------------------------------

## Перемножить все не чётные значения в диапазоне от 0 до введенного пользователем числа(R);

from functools import reduce
 
print("2.")

R = int(input("Введите ваше число"))
print(reduce(lambda x, y: x * y, range(1, R, 2)))

##---------------------------------------------

##Дано N чисел. Найти количество положительных чисел среди них; N рандомное число

from random import randint

print("3.")

N = randint(-50, 50)
k=0
for i in range(N):
    if N>0:
        k=k+1
print("Положительные числа из вашего случайного числа: ")
print(k)

##------------------------------------------------

## Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print("3.")

n = int(input("Введите число: "))
even=odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))

##------------------------------------

## Найти сумму ряда чисел от A до B. Полученный результат вывести на экран;

print("4.")

A=int(input("Введите число A: "))
B=int(input("Введите число B: "))

s=0

while A<=B:
    
    s=A+s

    A=A+1
print ("Сумма чисел от A до B = ", s)