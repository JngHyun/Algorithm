import sys
#sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
A = list(map(int,input().split()))
cnt=0
lt,rt = 0,1
tot = A[0]
while True:
    if tot < m:
        if rt<n:
            tot+=A[rt]
            rt+=1
        else:
            break
    elif tot == m:
        cnt += 1
        tot-=A[lt]
        lt+=1
    else:
        tot-=A[lt]
        lt+=1

print(cnt)







    

