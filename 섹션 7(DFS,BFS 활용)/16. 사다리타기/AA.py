import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/16. 사다리타기/in2.txt')
sys.setrecursionlimit(10**6) 
dx = [-1,1,0]
dy = [0,0,1]

def DFS(x,y):
    check[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and check[x][y-1] ==0:
            DFS(x,y-1)
        elif y+1<10 and board[x][y+1]==1 and check[x][y+1] ==0:
            DFS(x,y+1)
        else:
            DFS(x-1,y) 



if __name__ =='__main__':
    board = [list(map(int,input().split())) for _ in range(10)]
    check = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9,y)
