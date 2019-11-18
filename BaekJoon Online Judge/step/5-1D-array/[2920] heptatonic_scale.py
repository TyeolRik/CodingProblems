# https://www.acmicpc.net/problem/2920

import sys

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

input_list = list(map(int, sys.stdin.readline().rstrip().split()))

correct_ascending_count = 0
correct_descending_count = 0

for i in range(8):
    if ascending[i] == input_list[i]:
        correct_ascending_count = correct_ascending_count + 1
    else:
        break

for i in range(8):
    if descending[i] == input_list[i]:
        correct_descending_count = correct_descending_count + 1
    else:
        break

if correct_ascending_count == 8:
    print("ascending")
elif correct_descending_count == 8:
    print("descending")
else:
    print("mixed")