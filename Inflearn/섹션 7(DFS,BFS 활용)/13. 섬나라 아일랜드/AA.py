import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/13. 섬나라 아일랜드/in5.txt')
#DFS
def DFS(x,y):
    global cnt
    for k in range(8):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<n and s[xx][yy] ==1:
            s[xx][yy] =0
            DFS(xx,yy)
            
if __name__ =='__main__':
    n =int(input())
    s = [list(map(int,input().split())) for _ in range(n)]
    dx = [1,0,-1,0,-1,1,1,-1]
    dy = [0,-1,0,1,-1,-1,1,1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1:
                s[i][j]=0
                cnt+=1
                DFS(i,j)
                
    print(cnt)
