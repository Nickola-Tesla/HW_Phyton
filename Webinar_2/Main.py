
print('The first task')
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random
import math
coin = int(input("Количество монет:  "))

head = random.randint(0, coin)
print(head)

k = 0
for i in range(coin):
    v = int(input())
    if v == 1:
        k += 1
print(k if k<coin/2 else coin-k)





print('The second task')
#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа

num_s = int(input("Сумма загаданных чисел:  "))
num_p = int(input("Произведение загаданных чисел:  "))

diskriminant = num_s*num_s - num_p*4
if diskriminant < 0 :
    print("Таких чисел нет")
else :
    num_x1 = int((num_s + math.sqrt(diskriminant)) / 2)
    num_x2 = int((num_s - math.sqrt(diskriminant)) / 2)
    print(num_x1, num_x2)


print('The third task')   
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("ВВедите число N: "))

count = 0
result = 1
while result < number :
    result = 2**count
    count += 1
    if result >= number :
        break
    print(result)