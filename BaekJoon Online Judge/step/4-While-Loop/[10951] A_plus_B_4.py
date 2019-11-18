# https://www.acmicpc.net/problem/10951

import sys

a = []

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)