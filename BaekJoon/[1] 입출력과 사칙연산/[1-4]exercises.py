
# 1000. A B 입력받아 A+B 출력

'''
a = input().split()
b =[]
for i in a:
    b.append(int(i))
print(sum(b))
'''

# In[47]:


a = input().split()
A,B = [int(x) for x in a]
print(A+B)


# In[ ]:


# 1001. A-B


# In[52]:


a = input().split()

sum = sum([int(x) for x in a])
print(sum)


# In[54]:


inputs = input().split()
a, b= [int(x) for x in inputs]

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


# In[56]:


inputs = input().split()
A,B,C = [int(x) for x in inputs]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


# In[63]:


input1 = int(input())
input2 = list(input())

a, b, c= [int(x) for x in input2]

nr3 = input1 * c
nr4 = input1 * b
nr5 = input1 * a
nr6 = nr3 + nr4*10 + nr5*100

print(nr3)
print(nr4)
print(nr5)
print(nr6)


# # 2단계 if문

# In[2]:


#1330 두 수 비교하기

inputs = input().split()
a, b = [int(x) for x in inputs]
if a> b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')


# In[3]:


#9498 시험성적

score = int(input())
if score>=90:
    print('A')
elif score >=80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60 :
    print("D")
else:
    print('F')


# In[5]:


#2753 윤년

year = int(input())
if (year%4 == 0 and year%100 != 0) or year%400==0:
    print('1')
else:
    print('0')


# In[7]:


#14681 사분면고르기
num1 = int(input())
num2 = int(input())

if num1>0:
    if num2>0:
        print('1')
    else:
        print('4')
else:
    if num2>0:
        print('2')
    else:
        print('3')


# In[12]:


#2884 알람시계 45분 일찍 설정
time = input().split()
h,m=[int(x) for x in time]

if m>= 45:
    print(h, m-45)
else:
    if h!=0:
        print(h-1, m+15)
    else:
        print(23, m+15)


# # 3단계. for문

# In[18]:


# 2739. 구구단

N = int(input())

for i in range(1,10):
    print(N, '*', i, '=', N*i)


# In[23]:


#10950 A+B-3

T = int(input())
for i in range(T):
    test = input().split()
    a,b = [int(x) for x in test]
    print(a+b)


# In[29]:


#8393 합
n = int(input())
hap = [i for i in range(n+1)]
print(sum(hap))


# In[ ]:


# 15552. 빠른 A+B

import sys
T = int(input())
for i in range(T):
    A, B = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(A + B)


# In[39]:


#2741 N 찍기
N = int(input())
for i in range(1,N+1):
    print(i)


# In[45]:


#2742 기찍 N

N = int(input())
for i in range(N, 0, -1):
    print(i)


# In[101]:


# 11021 A+B-7

T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    print('Case #%s: %s'%(i+1, A+B))


# In[102]:


# 11022 A+B-8

T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print('Case #%s: %s + %s = %s'%(i+1, A, B, A+B))


# In[56]:


#2438 별찍기-1
N = int(input())
for i in range(1,N+1):
    print('*'*i)


# In[62]:


#2439 별찍기 우측정렬
N = int(input())
for i in range(1,N+1):
     print(('*'*i).rjust(N))


# In[3]:


#11 #10871 x보다 작은 수
N, X = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if i < X:
        print(i)





# # while문

# In[96]:


#1 #10952 A+B-5

while True:
    a,b = map(int,input().split())
    if a == 0 and b ==0:
        break
    print(a+b)


# In[97]:


#2 # 10951 A+B -4
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break
# while 문에는 반드시 break 를 걸어줘야한다.
# 정수형이 아닌 형태의 무언가 들어왔을 때는 while문을 멈춘다.


# In[94]:


#3 #1110 더하기 사이클


# In[ ]:





# In[ ]:




