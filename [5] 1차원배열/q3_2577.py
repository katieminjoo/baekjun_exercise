a = int(input())
b = int(input())
c = int(input())
d = a*b*c
d_list = list(str(d))

for i in range(10):
    num = d_list.count(str(i))
    print(num)