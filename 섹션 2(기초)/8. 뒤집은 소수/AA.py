import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
nums = list(input().split())


def reverse(x):
    res=""
    sum=0
    for i in range(len(x)-1,-1,-1):
        sum+=int(x[i])
        if sum !=0:
            res+=x[i]
    return res

def isPrime(x):
    cnt=0
    x = int(x)
    for i in range(1,x+1):
        if x%i == 0 :
            cnt+=1
    if cnt==2:
        return(x)
    else: pass
            
for x in nums:
    y = reverse(x)
    z = isPrime(y)
    if z != None:
        print(z,end=" ")

