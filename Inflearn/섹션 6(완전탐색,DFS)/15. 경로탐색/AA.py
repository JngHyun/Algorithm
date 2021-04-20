import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/15. 경로탐색/in1.txt')

# 주석 풀면 경로들 모두 출력해주는 코드로 변경

def DFS(x):
    global cnt
    if x==n:
        cnt += 1
        #print(*res,end=' ')
        #print()
        return
    else:
        for i in range(1,n+1):
            if g[x][i] == 1 and ch[i] == 0:
                ch[i] = 1
                #res.append(i)
                DFS(i)
                #res.pop()
                ch[i]=0 #돌아가면서 check 풀어주고 원소 내보내기


if __name__ == '__main__':
    n,m = map(int,input().split())

    g=[[0]*(n+1) for _ in range(n+1)]

    for i in range(m):
        a,b = map(int,input().split())
        g[a][b] = 1

    cnt = 0
    #res = list()
    #res.append(1)
    ch = [0]*(n+1) # 한번 방문한 노드는 다시 방문하지 않도록 체크
    ch[1] = 1
    DFS(1)
    print(cnt)




