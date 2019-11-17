# https://www.acmicpc.net/problem/10817

a = [int(i) for i in list(input().split())]
a.sort()
print(a[len(a) - 2])