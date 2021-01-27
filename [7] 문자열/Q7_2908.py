# 상수 a,b를 받고 그 수를 전부 역순으로 취한뒤, 어떤 수가 더 큰지 출력하기.

A, B = map(str, input().split())
L_A = [i for i in A]
L_B = [j for j in B]
# 리스트를 역순으로 바꿔주는 함수 : 리스트명.reverse()
# but ! return값은 없으므로 그냥 적용하면 본 리스트 자체가 바뀜
L_A.reverse()
L_B.reverse()
# 리스트 내의 문자열을 하나로 합쳐주는 join
# 사용법
# : ''.join(리스트명)
RA = int(''.join(L_A))
RB = int(''.join(L_B))

if RA > RB :
    print(RA)
else:
    print(RB)
