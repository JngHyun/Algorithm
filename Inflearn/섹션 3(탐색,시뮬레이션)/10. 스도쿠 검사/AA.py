import sys
sys.stdin = open("input.txt","rt")

a = [list(map(int,input().split())) for _ in range(9)]

dx = [0,-1,0,1,0,-1,1,-1,1]
dy = [0,0,-1,0,1,1,-1,-1,1]

for i in range(9):
    if len(set(a[i][:])) == 9 & len(set(a[:][i])) == 9:
        for t in range(1,9,3):    
            for p in range(1,9,3):
                if len(set([a[t+dx[k]][p+dy[k]] for k in range(9)])) == 9:
                    res = 1
                else:
                    res = 0
                    break
    else:
        res = 0
        break

if res == 1: print("YES")
else: print("NO")




