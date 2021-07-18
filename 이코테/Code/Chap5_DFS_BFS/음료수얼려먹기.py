import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap5_DFS_BFS/input.txt')

'''
n,m크기의 얼음틀이 있다. 구멍이 뚫려 있는 부분은 0 칸막이 부분은 1이다
구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우 1개의 얼음이 생성된다고 할 때
총 몇개의 아이스크림을 만들 수 있는 지 구해라

4 5
00110
00011
11111
00000

'''

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1
print(result)