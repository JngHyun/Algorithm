import sys
#sys.stdin = open("input.txt","rt")

s = list(range(1,21))

for i in range(10):
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    for j in range((b-a+1)//2):
        s[a+j],s[b-j] = s[b-j],s[a+j]
for x in s:
    print(x,end=' ')






    

