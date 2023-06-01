
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list_1[::2])

print(len(list_1))
print(set(list_1))
print(tuple(list_1))
setty = set(list_1)
setty.discard(5)
print(setty)

a = 2
if a == 2:
    print(a / 0)