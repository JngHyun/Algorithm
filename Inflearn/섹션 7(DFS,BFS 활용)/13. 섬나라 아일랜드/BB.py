import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/13. 섬나라 아일랜드/in5.txt')
# BFS
dx = [1,0,-1,0,-1,1,1,-1]
dy = [0,-1,0,1,-1,-1,1,1]
n = int(input())
board=[list(map(int,input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i,j))
            while Q:
                tmp =Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x,y))
            cnt+=1
print(cnt)


                
