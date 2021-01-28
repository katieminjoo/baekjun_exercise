# 크로아티아 알파벳

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()

for i in alpha:
    string = string.replace(i,'a')
print(len(string))