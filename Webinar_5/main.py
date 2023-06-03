
#def fib(n):
#    if n in (1, 2):
#        return 1
#    return fib(n - 1) + fib(n - 2)
    
#print(fib(10))

#f = int(input("Введите количество оценок: "))
#l = []
#for i in range(f):
#    l.append(int(input("Введите оценку: ")))


##l = [5, 1, 5, 3, 2, 5, 5, 5]
#for i in range(len(l)):
#  if l[i] == max(l):
#    l[i] = min(l)
#print(l)

#n = int(input("Введите число: "))
#x = 0
#for i in range(2, n // 2 + 1):
#    if (n % i == 0):
#        x = x + 1
#if (x <= 0):
#    print("Простое")
#else:
#    print("Не простое")

f = int(input("Введите количество чисел последовательности: "))
list_1 = []
for i in range(f):
    list_1.append(int(input("Введите число: ")))

list_r = (list_1[::-1])
print(list_1)
print(list_r)