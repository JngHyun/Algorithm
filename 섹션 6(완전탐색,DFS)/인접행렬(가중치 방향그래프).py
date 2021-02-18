
'''
무방향 그래프
''' 
# 행 번호에서 열 번호로 이동한다.

# a -> b , b -> a /  방향이 없으니 연결되어 있으면 둘다 이동 가능
# g[a][b] = 1
# g[b][a] = 1

import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/무방향input.txt','r')
n,m = map(int,input().split()) # n: 노드번호, m: 간선의 개수
g = [[0]*(n+1) for _ in range(n+1)] # g: graph

for i in range(m): #m개의 간선정보 들어온다
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1
# 행 별 1로 check된 열이 갈 수 있는 노드

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print()


print()

'''
가중치 방향 그래프
'''
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/가중치방향input.txt','r')
n,m = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    g[a][b] = c

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()

