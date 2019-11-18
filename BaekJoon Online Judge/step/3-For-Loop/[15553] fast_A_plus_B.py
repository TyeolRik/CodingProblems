# https://www.acmicpc.net/problem/15552

import sys

a = int(sys.stdin.readline().rstrip())
b = []
for i in range(a):
    b.append(sys.stdin.readline().split())
    print(int(b[i][0]) + int(b[i][1]))