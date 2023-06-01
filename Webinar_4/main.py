
#f_dict = {'Suslick':+7965586521, 'Surock':[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 'Homyak':+7965845212}

#print(f_dict['Suslick'])
#print(f_dict.get('Surock'))

#Напишите программу, которая принимает на вход
#строку, и отслеживает, сколько раз каждый символ
#уже встречался. Количество повторов добавляется к
#символам с помощью постфикса формата _n.
#s = 'a a a b a c b b d'.split()

#s = 'a a a b a c b b d'.split()
#l = {}
#r = ''
#for i in range(len(s)):
#    if s[i] not in l.keys():
#        l[s[i]] = 1
#        r += f'{s[i]} '
#    else:
#        r += f'{s[i]}_{l[s[i]]} '
#        l[s[i]] += 1
#print(r)

#s = 'a a a b a c b b d d'.split()
#r = ''

#for i, letter in enumerate((s)):
#    if s[:i].count(letter)<1:
#        r+=letter+' '
#    else:
#        r+=f'{letter}_{s[:i].count(letter)} '
#print(r)

#Пользователь вводит текст(строка). Словом считается
#последовательность непробельных символов идущих
#подряд, слова разделены одним или большим числом
#пробелов. Определите, сколько различных слов
#содержится в этом тексте.
#Input: She sells sea shells on the sea shore The shells
#that she sells are sea shells I'm sure.So if she sells sea
#shells on the sea shore I'm sure that the shells are sea
#shore shells
#Output: 13

#s = "She sells, sea shells on the sea shore. The shells\
# that she sells are sea shells! I'm sure So if she sells sea \
#shells on the sea shore? I'm sure that\n the shells are sea \
#shore shells"
#r = [i.strip('.,?!\n').lower() for i in s.split()]
#r = set(r)
#print(r)
#print(len(r))

#Ваня и Петя поспорили, кто быстрее решит
#следующую задачу: “Задана последовательность
#неотрицательных целых чисел. Требуется определить
#значение наибольшего элемента
#последовательности, которая завершается первым
#встретившимся нулем (число 0 не входит в
#последовательность)”. Однако 2 друга оказались не
#такими смышлеными. Никто из ребят не смог до
#конца сделать это задание. Они решили так: у кого
#будет меньше ошибок в коде, тот и выиграл спор. За
#помощью товарищи обратились к Вам, студентам.

print('Иван: ')
n = int(input())
max_number = 1000
while n != 0:
    n = int(input())
    if max_number > n:
        max_number = n
print(max_number)

print('Петр: ')
n = int(input())
max_number = -1
while n < 0:
    n = int(input())
    if max_number < n:
        n = max_number
print(n)

print('Решение: ')
num = int(input())
max = num
while num != 0:
    if num > max and num != 0:
       max = num
    num = int(input())
print(f'{max = }')