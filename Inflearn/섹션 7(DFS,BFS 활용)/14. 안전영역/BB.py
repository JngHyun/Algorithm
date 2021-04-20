import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/14. 안전영역/in4.txt')
sys.setrecursionlimit(10**6)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y,h):
    ch[x][y]=1
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] >=h and ch[xx][yy]==0:
            DFS(xx,yy,h)


if __name__=="__main__":
    n = int(input())
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):#높이가 100이면 안전지역이 0이라 돌릴 필요 없음/ 하지만 0은 돌려야함
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] >=h and ch[i][j] ==0:
                    cnt+=1
                    DFS(i,j,h)
        
        res = max(res,cnt)
        if cnt ==0: #최대 높이까지만 돌리면 됨
            break
    print(res)

