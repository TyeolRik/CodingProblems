# https://www.acmicpc.net/problem/2562

import sys

input_list = []
for i in range(9):
    input_list.append(sys.stdin.readline().rstrip())

maximum = max(input_list)
print(maximum)
print(input_list.index(maximum) + 1)