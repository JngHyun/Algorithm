import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/15. 토마토/in4.txt')

dx=[1,0,-1,0]
dy=[0,1,0,-1]

m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
Q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] ==1:
            Q.append((i,j))

while Q:
    x,y = Q.popleft()
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<m and box[xx][yy] ==0:
            box[xx][yy]=1
            dis[xx][yy] = dis[x][y] +1
            Q.append((xx,yy))
    
flag = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            flag=1
res =0
if flag ==0:
    for i in range(n):
        for j in range(m):
            if dis[i][j]>res:
                res = dis[i][j]
    print(res)
else:
    print(-1)

