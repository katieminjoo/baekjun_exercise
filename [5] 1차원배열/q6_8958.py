n = int(input())
for i in range(n):
    ox = input()
    ox_list = list(ox)
    score = 0
    sum_score = 0
    for j in ox_list:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)