import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/12. 단지번호붙이기/in3.txt')
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    board[x][y]=0
    cnt+=1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx,yy)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int,input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i,j)
                res.append(cnt)
    res.sort()
    print(len(res))
    print(*res,sep='\n')
