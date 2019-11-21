# https://www.acmicpc.net/problem/10809

import sys

alphabet = list("abcdefghijklmnopqrstuvwxyz")
position = [-1 for i in range(26)]
S = list(sys.stdin.readline().rstrip());

for i in range(len(S) - 1, -1, -1):
    position[ord(S[i]) - ord('a')] = i

for each in position:
    print(each, end = ' ', flush = True)