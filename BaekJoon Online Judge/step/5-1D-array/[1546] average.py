# https://www.acmicpc.net/problem/1546

import sys

N = int(sys.stdin.readline().rstrip())
score_list = list(map(int, sys.stdin.readline().rstrip().split()))
max_score = max(score_list)
for i in range(len(score_list)):
    score_list[i] = score_list[i] / max_score * 100

print(sum(score_list)/len(score_list))