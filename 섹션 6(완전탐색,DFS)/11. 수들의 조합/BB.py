import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/11. 수들의 조합/in5.txt')

def DFS(L,s,sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s,n):
            DFS(L+1,i+1,sum+a[i])

if __name__=='__main__':
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = 0
    DFS(0,0,0)
    print(cnt)