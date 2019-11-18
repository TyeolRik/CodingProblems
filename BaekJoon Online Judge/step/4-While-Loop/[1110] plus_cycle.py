# https://www.acmicpc.net/problem/1110

import sys

a = int(sys.stdin.readline().rstrip())

def one_cycle(int_input):
    string_list = []
    _sum = 0
    # 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고 각 자리의 숫자를 더한다.
    if int_input < 10:
        _sum = int_input % 10
    else:
        _sum = int(int_input / 10) + int(int_input % 10)
    
    return (int_input % 10) * 10 + _sum % 10

initial_number = a
count = 0
while one_cycle(a) != initial_number:
    count = count + 1
    a = one_cycle(a)

print (count + 1)
