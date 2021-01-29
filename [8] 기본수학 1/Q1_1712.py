FC, VC, Price = map(int, input().split())
if VC >= Price :
    print('-1')
else:
    print(int(FC/(Price-VC)+1))