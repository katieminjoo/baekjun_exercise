# 문자열 반복
T = int(input())
for i in range(T):
    num, character = input().split()
    for j in character:
        print(str(j)*int(num), end='')
    print()
