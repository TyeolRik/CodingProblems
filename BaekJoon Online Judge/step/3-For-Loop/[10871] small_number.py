# https://www.acmicpc.net/problem/10871

a, b = input().split()
c = list(input().split())

for i in range(len(c)):
    if int(c[i]) < int(b):
        print(int(c[i]), end = " ", flush = True)