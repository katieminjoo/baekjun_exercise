"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""
n = int(input())
group = 0
for i in range(n):
    word = input()
    cnt = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]: # 붙어있는 a,b 두 문자가 다르면
            word_list = word[j+1:] # b부터 끝까지 리스트로 저장
            if word_list.count(word[j]) > 0: #그 리스트에서 a를 찾아서 한개라도 있으면 > 붙어있지않은 a가 하나 더 있는거니까 그룹단어가 아님
                cnt += 1
    if cnt == 0:
        group += 1
print(group)