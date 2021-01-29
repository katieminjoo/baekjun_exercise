# 벌집문제

# 짧게 적은 코드
n = int(input())
bee_house = 1
layer = 1
while n>bee_house:
    bee_house += 6*layer
    layer += 1
print(layer)

N = int(input())
cnt = 1
while N > 1:
    N -= (6 * cnt)
    cnt += 1
print(cnt)
-------------------------------------------------------------------
# 이게 내가 제일 이해하기 쉬운 코드

n = int(input())
n_max = 7
n_add = 6
n_result = 2
while True:
    if n == 1:
        n_result = 1
        break
    if n <= n_max :
        break
    else:
        n_add += 6
        n_max += n_add
        n_result += 1
print(n_result)

# 재귀함수 이용

import sys
# Python의 경우, 재귀함수 깊이 제한 늘리기 필요
sys.setrecursionlimit(10**5)

N = int(input())

def bee_house(N, cnt):
    if N <= 1:
        print(cnt)
        return
    else:
        bee_house(N-(6*cnt), cnt+1)

bee_house(N, 1)