import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/6. 중복순열 구하기/in1.txt')
def DFS(x,res):
    global cnt
    if x == m:
        for i in range(m):
            print(res[i] , end=' ')
        print()
        cnt +=1
        return
    
    else:
        for i in range(n):
            res[x] = i+1
            DFS(x+1,res)


if __name__=='__main__':
    n,m = map(int,input().split())
    res = [0] * m
    cnt = 0
    DFS(0,res)
    print(cnt)
