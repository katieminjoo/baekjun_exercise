# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 첫 시도
c = int(input())
for i in range(c):
    case = list(map(int, input().split()))
    average = (sum(case)-case[0])/(len(case)-1)
    count = 0
    for j in case:
        if j > average :
            count += 1
    r = (count/(len(case)-1))*100
    print("%.3f" %r+'%')
# it worked, but maybe i need to make it simple.

# 2nd
c = int(input())
for i in range(c):
    case = list(map(int, input().split()))
    avg = sum(case[1:])/case[0]
    cnt = 0
    for score in case[1:]:
        if score>avg:
            cnt += 1
    r = cnt/case[0]*100
    print("%.3f" %r+'%')