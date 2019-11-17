# https://www.acmicpc.net/problem/10950

a = int(input())
b = []
for i in range(a):
    b.append(input().split())
for i in range(a):
    print(int(b[i][0]) + int(b[i][1]))