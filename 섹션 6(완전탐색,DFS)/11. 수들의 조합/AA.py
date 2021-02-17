import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/11. 수들의 조합/in5.txt')

def DFS(x,s):
    global cnt
    if x==k:
        if sum(res)%m==0:
            cnt += 1
        return
    else:
        for i in range(s,n+1):
            res[x] = l[i-1]
            DFS(x+1,i+1)

if __name__=='__main__':
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0,1)
    print(cnt)