#������ 22: ���� ��� ��������������� ������ ����� ����� (����� ����, � ������������).
#������ ��� ���������� � ������� ����������� ��� �� �����, ������� ����������� � ����� �������.
#������������ ������ 2 �����. n - ���-�� ��������� ������� ���������.
#m - ���-�� ��������� ������� ���������. ����� ������������ ������ ���� �������� ��������.


n = int(input("������� ���������� ��������� ������� ���������"))
m = int(input("������� ���������� ��������� ������� ���������"))

set_1 = set(int(input(f"������� {n} ��������� ������� ���������")) for _ in range(n))
set_2 = set(int(input(f"������� {m} ��������� ������� ���������")) for _ in range(m))
result_set = sorted(set_1.intersection(set_2))
print(set_1)
print(set_2)
print(result_set)

#������ 24: � ���������� ��������� � ������� ���������� �������. ��� ������ �� ������� ������, ������ ����� �������� ������ �� ����������.
#����� �������, � ������� ����� ���� ����� ��� ��������. ����� �� ������ ������ N ������.
#��� ����� �������� ������ ������������, ������� �� ������� ����� �� ��� ������� ��������� ����� ���� � �� i-�� ����� ������� ai ����.
#� ���� ���������� ��������� �������� ������� ��������������� ����� �������.
#��� ������� ������� �� ������������ ������ � ���������� ���������� �������. ���������� ������ �� ���� �����,
#�������� ��������������� ����� ��������� ������, �������� ����� � ����� ����� � � ���� �������� � ���.
#�������� ��������� ��� ���������� ������������� ����� ����, ������� ����� ������� �� ���� ����� ���������� ������,
#�������� ����� ��������� ������ �������� �� ������� ����� ������.

n = int(input("������� ���������� ������ "))
lst = []
for i in range(n):
    x = int(input("������� ���������� ���� �� ����� "))
    lst.append(x)
x = 0
lst += lst[:2]
for i in range(n):
    x = max(x, lst[i] + lst[i + 1] + lst[i + 2])
print(x)
