
from itertools import count


#print('Привет Мир!')
#list_1 = [];
#c = list(map(str, input().split))
# d = [a for a in input().split()]
# 
#l = list('abcdef')
#print(l)
#i = 0

#list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
#print(list(list_1))
#list_1 = set(list_1)
#for a in range(len(list_1)):
#    i = i + 1
#print(list(setty))
#print(f'количество различных символов равно =  {i}')

#d = [int(a) for a in input("Введите набор символов: ").split()]
#print(f'количество различных символов равно =  {len(set([int(a) for a in input("Введите набор символов: ").split()]))}')

#a = [int(a) for a in input().split()]
#k = int(input())
#i = 0
#while i < k:
#    poped = a.pop()
#    a.insert(0, poped)
#    i += 1
#print(a)

#a = [int(a) for a in input().split()]
#i = 0
#c = 0
#while i < len(a):
#    if a[i]> a[i-1]:
#        c+=1
#    i+=1   
#print(c)


#a = [int(a) for a in input('Введите последовательность: ').split()]
#count = 0
#for i in range(len(a)):
#    if a[i] > a[i - 1]:
#        count += 1
#    i += 1
#print(f'Количествоэлементов массива, больших предыдущего равно {count}')
N = int(input('Введите необходимое количество элементов: '))
A = [int(input('сравниваем с числом: ')) for i in range(1, N+1)]
X = int(input('К какому числу нужно найти ближайшее: '))
