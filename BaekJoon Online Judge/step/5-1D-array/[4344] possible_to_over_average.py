# https://www.acmicpc.net/problem/4344

import sys

size_of_test_case = int(sys.stdin.readline().rstrip())

for _test in range(size_of_test_case):
    test_case = list(map(int, sys.stdin.readline().rstrip().split()))
    average = (sum(test_case) - test_case[0]) / test_case[0]
    how_many = 0
    for i in range(1,len(test_case)):
        if test_case[i] > average:
            how_many = how_many + 1
    print(format(round((how_many / test_case[0] * 100), 3), ".3f"), end = '', flush = True)
    print("%")