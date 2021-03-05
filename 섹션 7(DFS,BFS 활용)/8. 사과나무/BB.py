import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/8. 사과나무/in2.txt')

#사과 밭의 중심을 기준으로 레벨 탐색에서 상하좌우를 탐색한다.

dx = [-1,0,1,0]#상하좌우 좌표이동
dy = [0,1,0,-1]
n = int(input())
a= [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)] #한번들어간 것은 다시 들어가지 않게 체크
sum=0
Q = deque()
ch[n//2][n//2]=1 #중심점 체크
sum += a[n//2][n//2] #중심점 합하기
Q.append((n//2,n//2)) #Q에 중심점 좌표 넣기
L=0 #level
while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size):#레벨 사이즈
        tmp = Q.popleft()
        for j in range(4):#4방향으로 뻗어가기
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] ==0: #한번도 방문한적이 없다면
                sum+=a[x][y] #더하기
                ch[x][y]=1 #체크하기
                Q.append((x,y)) #que 에 레벨 넣기
    L+=1
print(sum)