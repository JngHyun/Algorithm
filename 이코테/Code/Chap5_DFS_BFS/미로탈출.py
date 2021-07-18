import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap5_DFS_BFS/input.txt')

'''
n,m크기의 직사각형 형태 미로
괴물이 있는 부분은 0 괴물이 없는 부분은 1일 때, 미로를 탈출하기 위해 움직이어야 하는 최단거리를 구하시오
(시작칸(1,1)과 마지막 칸(n,m)을 포함하여 센다.)

5 6
101010
111111
000001
111111
111111
'''
from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<=-1 or nx>=n or ny <= -1 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))      
    return graph[n-1][m-1]

print(bfs(0,0))