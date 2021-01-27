# 다이얼전화기로 전화거는데 걸리는 시간 구하기
# 숫자 2 : 3초, 3: 4초...
# 숫자 2 : abc, 3 : def ...

L = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0
for i in word:
    for j in L:
        if i in j:
            time += L.index(j) + 3
print(time)

