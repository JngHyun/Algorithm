import sys
from collections import deque
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/7. 송아지 찾기/in5.txt')

#BFS
#레벨탐색 - que사용
#깊이우선 탐색이 아니라 같은 레벨에서의 말단 노드들 끼리 비교

import time
st = time.time()
MAX = 100000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now==m: #도착지점 발견
        break
    for next in(now-1,now+1,now+5): #한 레벨의 노드에서 3개로 뻗어나감
        if 0<next<=MAX:
            if ch[next]==0: #과거에 방문하지 않았을 때
                dQ.append(next)
                ch[next]=1
                dis[next] = dis[now]+1
            
print(dis[m])
et = time.time()
print(et-st)