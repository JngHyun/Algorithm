import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
m = []
l,r=0,0

for i in range(n):
    m.append(list(map(int,input().split())))
    l += m[i][i]
    r += m[i][n-i-1]
row = [sum(x) for x in m]
col = [sum([x[i] for x in m]) for i in range(5)]

res=max(max(row),max(col),l,r)
print(res)

    
    