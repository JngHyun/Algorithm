import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/14. 안전영역/in5.txt')
dx = [1,0,-1,0]
dy = [0,1,0,-1]
sys.setrecursionlimit(10**6)
def DFS(x,y,h):
    global cnt
    check[x][y] = 1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]>=h and check[xx][yy]!= 1:
            DFS(xx,yy,h)

if __name__=='__main__':
    n = int(input())
    board=[]
    height = []
    res = 0
    for _ in range(n):
        a = list(map(int,input().split()))
        board.append(a)
        height+=a
    for h in set(height): 
        check = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] >= h and check[i][j]==0:
                    cnt+=1
                    DFS(i,j,h)
        res = max(res,cnt)
    print(res)


    
