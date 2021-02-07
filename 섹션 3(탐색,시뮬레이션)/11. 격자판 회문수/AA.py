import sys
sys.stdin = open("input.txt","rt")

a = [list(map(int,input().split())) for _ in range(7)]

def check(l):
    return all(l[i] == l[5-i-1] for i in range(2))

res=0
for j in range(7):
    for i in range(2,5):
        if check(a[j][i-2:i+2+1]):
            res +=1
        if check([a[k][j] for k in range(i-2,i+2+1)]): 
            res +=1

print(res)
    




