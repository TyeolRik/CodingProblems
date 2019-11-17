# https://www.acmicpc.net/problem/2884

a, b = input().split()
a = int(a)
b = int(b)

b = b - 45 # 45분 일찍 맞추기
if b < 0:
    b = b + 60
    a = a - 1
    if a < 0:
        a = a + 24

print(a, b)
