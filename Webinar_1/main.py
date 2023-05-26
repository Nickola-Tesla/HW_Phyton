print('The first task')
number = int(input("Введите трёхзначное число: "))
summ = 0
while number > 0:
    summ += number % 10
    number //= 10
print(summ)

print('The second task')
s = int(input("Введите число журавликов, которые изготовили Петя, Катя и Серёжа: "))
while s % 6 > 0:
    s = int(input("Вы ввели некорректное число журавликов, повторите ввод: "))
print(f'{s} -> {s // 6}; {s // 3 * 2}; {s // 6}.')

print('The third task')
ticket = int(input("Введите номер билета: "))
while (ticket <= 99999) or (ticket > 999999):
     ticket = int(input("Вы ввели некорректный номер билета: "))

half1, half2 = 0, 0
summ = ticket
for i in range(3):
     half2 += summ % 10
     summ //= 10

for i in range(3):
     half1 += summ % 10
     summ //= 10
if half1 == half2:
     print(f'{ticket} -> yes')
else:
     print(f'{ticket} -> no')

print('The fourth task')
n = int(input("Введите длину шоколадки в дольках: "))
m = int(input("Введите ширину шоколадки в дольках: "))
k = int(input("Введите желаемое количество долек: "))

while k > (n * m) or k < 1:
      ticket = int(input("В шоколадке нет столько долек, подумайте и повторите ввод: "))
if k % n == 0 or k % m == 0:
      print(f'{n} {m} - {k} -> yes')
else:
      print(f'{n} {m} - {k} -> no')