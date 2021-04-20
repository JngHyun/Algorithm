import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/17. 피자 배달 거리/in1.txt')

def DFS(L,s):
    global res
    if L==m:
        sum = 0
        #집의 좌표
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            #4개 조합으로 선택된 피자집의 좌표
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2) + abs(y1-y2))
            #각집들의 피자거리 합 = 도시 피자거리
            sum+=dis
        if sum<res:
            res=sum


    else:
        for i in range(s,len(pz)):
            cb[L] = i
            DFS(L+1, s+1)

if __name__ =='__main__':
    n, m = map(int,input().split()) # m : 살아남을 피자집의 정보
    board = [list(map(int,input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000000
    # 피자집과 집 모으기
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i,j))
            if board[i][j]==2:
                pz.append((i,j))
    
    DFS(0,0)        
    print(res)

    