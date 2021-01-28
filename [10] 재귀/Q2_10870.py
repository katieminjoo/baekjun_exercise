# 피보나치 수열

n = int(input())
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n-1) + f(n-2)
print(f(n))