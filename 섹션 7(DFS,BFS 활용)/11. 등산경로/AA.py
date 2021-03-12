import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/11. 등산경로/in5.txt')
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def DFS(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0

    

if __name__ =='__main__':
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    cnt = 0
  
    max = -2147000000
    min = 2147000000
    for i in range(n):
        for j in range(n):
            tmp = board[i][j]
            if tmp < min:
                min = tmp
                sx = i
                sy = j
            if tmp > max:
                max = tmp
                ex = i
                ey = j
    ch[sx][sy]=1
    DFS(sx,sy)
    print(cnt)
            
 




