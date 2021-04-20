import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/14. 위상정렬/in1.txt')

#위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘
# 각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의 순서를 짜는 알고리즘

n,m=map(int,input().split())
 
# 진입 차수 : 해당 노드에 연결된 다른 노드 갯수
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dQ =deque()
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    degree[b] +=1

for i in range(1,n+1):
    if degree[i]==0:
        dQ.append(i)

while dQ:
    x = dQ.popleft()
    print(x,end=' ')
    for i in range(1,n+1):
        if graph[x][i]==1:
            degree[i] -= 1
            if degree[i]==0:
                dQ.append(i)
