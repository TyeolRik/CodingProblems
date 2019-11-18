# https://www.acmicpc.net/problem/10952

while True:
    a, b = input().split()
    a, b = int(a), int(b)
    if (a == 0) and (b == 0):
        break
    else:
        print(a + b)