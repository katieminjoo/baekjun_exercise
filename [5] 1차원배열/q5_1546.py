# 정수 n과 n개의 점수들을 받은다음, 가장 높은 점수로 다시 다 나누어 *100을 한 후 새 평균 구하기


n = int(input())
scores = list((map(int,input().split())))
h_score = max(scores)
new_scores=[]
for i in scores:
    new_scores.append(i/h_score*100)
print(sum(new_scores,0.0)/len(new_scores))