# https://www.acmicpc.net/problem/2577

import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
_calc = A * B * C

now_number = 0
count = 0
for i in range(10):
    for each_space in str(_calc):
        if now_number == int(each_space):
            count = count + 1
    print(count)
    now_number = now_number + 1
    count = 0
