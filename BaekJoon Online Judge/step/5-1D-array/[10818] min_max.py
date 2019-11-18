# https://www.acmicpc.net/problem/10818

import sys

input_number_size = int(sys.stdin.readline().rstrip())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(input_list), max(input_list))