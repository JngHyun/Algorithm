import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/9. 미로의 최단거리/in2.txt')

a = [list(map(int,input().split())) for _ in range(7)]

dx = [-1,0,1,0]#상하좌우 좌표이동
dy = [0,1,0,-1]
ch = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0)) 
a[0][0]=1 #한번 방문한 곳은 벽으로 만듬

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and a[x][y]==0:
            a[x][y]=1
            ch[x][y] = ch[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if ch[6][6]==0:
    print(-1)
else:
    print(ch[6][6])

    
    