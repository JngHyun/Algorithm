import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/9. 수열 추측하기/in5.txt')

def DFS(x):
    if x >= n:
        sum = 0
        for i in range(n):
            sum+=p[i]*b[i]
        if sum == f:
            print(*p,end=' ')
            sys.exit(0)
    
    else: 
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[x] = i
                DFS(x+1)
                ch[i]=0


if __name__=='__main__':
    n,f = map(int,input().split())
    p = [0]*n
    b = [1]*n
    ch = [0]*(n+1)
    for i in range(1,n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0)