# https://www.acmicpc.net/problem/8958

import sys

size_of_test_case = int(sys.stdin.readline().rstrip())


for i in range(size_of_test_case):
    input_text = str(sys.stdin.readline().rstrip())
    score = 0
    temp = 0
    for each in input_text:
        if each == "O":
            temp = temp + 1
            score = score + temp
        else:
            temp = 0
    print(score)

