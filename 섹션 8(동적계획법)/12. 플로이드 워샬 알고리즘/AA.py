import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/12. 플로이드 워샬 알고리즘/in1.txt')
#플로이드 워샬 : 모든 정점에서 모든 정점으로 가는 최단거리 구하는 알고리즘

if __name__=="__main__":
    n, m=map(int, input().split())
    dis=[[5000]*(n+1) for _ in range(n+1)] # M = 5000 : 한번에 갈 수 없는 경우는 큰 값으로 초기화 함
    #대각행렬 : 자기자신으로 가는 경우 0 으로 초기화
    for i in range(1, n+1):
        dis[i][i]=0 # i에서 j노드로 가는데 드는 최소비용값이 다이나믹 테이블 dis에 들어가게 됨
    #다이나믹 테이블  인접행렬 초기화 (한번에 갈 수 있는 경우)
    for i in range(m):
        a, b, c=map(int, input().split())
        dis[a][b]=c
    # i 에서 j 로 갈때 지나치는 노드들
    #플로이드 와샬 알고리즘 - 중요! 
    for k in range(1, n+1): # 중간에 거치는 노드 1 ~ n
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
                # 기존 비용과 i -> k -> j 비용을 비교해 교체해 줌 (k를 거쳐 가는 것) : 비용이 작은 경로 순으로 결정된다.
    #출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j]==5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()