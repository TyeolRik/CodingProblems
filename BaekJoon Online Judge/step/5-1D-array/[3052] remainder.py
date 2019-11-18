# https://www.acmicpc.net/problem/3052

import sys

a = []

for i in range(10):
    a.append(int(sys.stdin.readline().rstrip())%42)

print(len(list(set(a))))