# 분수찾기
x = int(input())
line = 1

# 전체 x번째가 몇번째라인에 몇번째 수 인지 알아내야함.
while x > line:
    x -= line
    line += 1

# 짝수 라인인 경우
if line % 2 == 0:
    a = x
    b = line - x + 1

# 홀수인경우
else:
    a = line - x + 1
    b = x

print(str(a)+'/'+str(b))