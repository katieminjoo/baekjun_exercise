# 한수 개수 구하기
# 한수 = 각 자리의 숫자끼리의 공차가 일정한 수, 1부터 99는 모두 한수

# 내 코드
n = int(input())
hansu = 0
for i in range(1, n+1):
    if i < 100:
        hansu += 1
    else:  # 101~999
        a, b, c = map(int, str(i))
        if a-b == b-c:
            hansu += 1
print(hansu)

# 비슷한 방식으로 리스트에서 추출해오는 방식

.# n = int(input())
# hansu = 0
# for i in range(1, n+1):
#     if i < 100:
#         hansu += 1
#     else:  # 101~999
#         L = list(map(int, str(i)))
#         if L[0] - L[1] == L[1] - L[2]:
#             hansu += 1
# print(hansu)

# 백,십,일의 자리 수를 나눗셈으로 꺼내오기
# def Han(n):
#     cnt = 0
#     if (n < 100):
#         return n
#     else:
#         for i in range(100, (n + 1)):
#             hund = (i // 100)
#             ten = ((i % 100) // 10)
#             one = ((i % 100) % 10)
#
#             if ((hund - ten) == (ten - one)):
#                 cnt += 1
#         return (99 + cnt)
#
#
# inp = int(input())
# res = Han(inp)
# print(res)
