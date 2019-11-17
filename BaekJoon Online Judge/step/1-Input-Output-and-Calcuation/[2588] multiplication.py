a = input()
b = input()
b_list = list(b)
b_list.reverse()
for i in range(0, len(b_list)):
    print(int(a) * int(b_list[i]))
print(int(a)*int(b))