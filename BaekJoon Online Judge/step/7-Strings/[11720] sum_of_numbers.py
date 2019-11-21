# https://www.acmicpc.net/problem/11720

import sys

size_of_inputs = int(sys.stdin.readline().rstrip());
inputs = list(sys.stdin.readline().rstrip());
total = 0
for i in range(size_of_inputs):
    total = total + int(inputs[i])

print(total)