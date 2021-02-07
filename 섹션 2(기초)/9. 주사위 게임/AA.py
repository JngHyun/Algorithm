import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
max =0
for i in range(n):
    tmp = sorted(input().split())
    a,b,c = map(int,tmp)
    if (a==b & b==c) :
        res=10000 + a * 1000
    elif a==b or a==c:
        res=1000+a*100
    elif b==c:
        res=1000+b*100
    else:
        res=c*100
    if res>=max:
        max=res

print(max)



