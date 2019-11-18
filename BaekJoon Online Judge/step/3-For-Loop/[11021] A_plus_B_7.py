# https://www.acmicpc.net/problem/11021

a = int(input())
for i in range(a):
    a, b = input().split()
    a, b = int(a), int(b)
    print("Case #{0}: {1}".format(i + 1, a + b))