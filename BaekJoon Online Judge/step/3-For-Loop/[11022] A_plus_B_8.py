# https://www.acmicpc.net/problem/11022

a = int(input())
for i in range(a):
    a, b = input().split()
    a, b = int(a), int(b)
    print("Case #{0}: {1} + {2} = {3}".format(i + 1, a, b, a + b))