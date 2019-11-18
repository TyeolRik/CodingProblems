# https://www.acmicpc.net/problem/2438

a = int(input())

for i in range(a):
    for k in range(a - (i + 1)):
        print(" ", end = '', flush = True)
    for j in range(i + 1):
        print("*", end = '', flush = True)
    print("")