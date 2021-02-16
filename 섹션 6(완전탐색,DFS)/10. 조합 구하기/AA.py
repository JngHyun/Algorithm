import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/10. 조합 구하기/in2.txt')

def DFS(x,s):
    global cnt
    if x==m:
        print(*res,sep=' ')
        cnt += 1
        return
    else:
        for i in range(s,n+1):
            res[x] = i
            DFS(x+1,i+1)


if __name__=='__main__':
    n,m=map(int,input().split())
    cnt = 0
    res = [0] * m
    DFS(0,1)
    print(cnt)
    