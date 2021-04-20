import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
c = []
p,q = 0,0
while(True):
    if a[p] <= b[q]:
        c.append(a[p])
        p+=1
    else:
        c.append(b[q])
        q+=1
    if p==n or q==m:
        break;
if p==n:
    c+=b[q:]
else:
    c+=a[p:]

print(c,end=' ')



    

