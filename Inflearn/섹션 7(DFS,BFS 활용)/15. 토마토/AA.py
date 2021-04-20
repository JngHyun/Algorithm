import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/15. 토마토/in5.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(m)]

Q = deque()
dis = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if box[i][j]==1:
            Q.append((i,j))

while Q:
    x,y = Q.popleft()
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<m and 0<=yy<n and box[xx][yy]==0:
            box[xx][yy]=1
            dis[xx][yy] = dis[x][y]+1
            Q.append((xx,yy))
        

flag = 1
for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            flag = 0
cnt = 0
if flag ==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > cnt:
                cnt = dis[i][j]
    print(cnt)
else:
    print(-1)




