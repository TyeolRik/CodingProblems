# https://www.acmicpc.net/problem/2675

import sys

T = int(sys.stdin.readline().rstrip())
inputs = []
for i in range(T):
    inputs.append(sys.stdin.readline().rstrip().split())
    R = int(inputs[i][0])
    S = list(inputs[i][1])
    for each_letter in S:
        for j in range(R):
            print(each_letter, end='',flush=True)
    print("");