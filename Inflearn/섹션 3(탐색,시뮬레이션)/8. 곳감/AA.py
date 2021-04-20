import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
N = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
M = [list(map(int,input().split())) for _ in range(m)]

for i in range(m):
    index = M[i][0]-1
    roll=M[i][2]
    if M[i][1] == 0:
        N[index] = N[index][roll:] + N[index][:roll]
    else:
        N[index] = N[index][-roll:] + N[index][:n-roll]

cen = n//2
res = N[cen][cen]

for j in range(cen):
    res+=sum(N[cen-j-1][cen-j-1:cen+j+2]) 
    res+=sum(N[cen+j+1][cen-j-1:cen+j+2])

print(res)