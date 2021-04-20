import sys
#ys.stdin = open("input.txt","rt")

n = int(input())

m = [list(map(int,input().split())) for _ in range(n)]

tot = sum(m[n//2])
for i in range(n//2):
    l = abs(n//2-i)
    r = abs(n//2+i)
    tot += sum(m[i][l:r+1])
    tot += sum(m[n-1-i][l:r+1])

print(tot)