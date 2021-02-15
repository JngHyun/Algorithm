import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/9. 수열 추측하기/in5.txt')

# 정답 후보 - 순열
# DFS는 순열을 구하기 위해 사용 됨

def DFS(L,sum):
    if L==n and sum==f:
        for x in p:
            print(x,end=' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1,sum+(p[L]*b[L]))
                ch[i]=0

if __name__ =='__main__':
    n,f = map(int,input().split())
    p=[0]*n
    b=[1]*n #이항계수 구하기 위한 준비
    ch=[0]*(n+1)
    for i in range(1,n):
        b[i] = b[i-1]*(n-i)//i #combination 사용해 이항계수 구하기
    #print(*b,end=' ')
    DFS(0,0)
    
# 1. 맨 위에 있는 수열은 은 n개의 다른 수로 이루어진 순열
# 2. 파스칼의 삼각형처럼 구현하여 한 숫자를 구하는 것은 이항계수를 각 수에 곱해주는 것과 같다는 규칙
# 3. 이항계수는 for i in range(n) nCi 로 구할 수 있다.