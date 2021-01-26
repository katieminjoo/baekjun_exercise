# 셀프넘버

L = set(range(1, 10001))
not_selfnumber = set()
for number in L:
    for str_number in str(number):
        number = number + int(str_number)
    not_selfnumber.add(number)

self_number = L - not_selfnumber
for i in sorted(self_number):
    print(i)