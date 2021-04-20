import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/2. 휴가/in1.txt')

def DFS(x,sum):
    global min
    if x == n+1: #종료지점 정확히 해야함
        if sum > min:
            min = sum
    else:
        if x + t[x] <= n+1: #현재 날짜에 잡힌 상담을 하는 것
            DFS(x+t[x],sum+p[x])
        DFS(x+1,sum)

if __name__ =='__main__':
    n = int(input())
    t = [0]*(n+1)
    p = [0]*(n+1)
    min = -2147000000
    sum = 0
    for i in range(1,n+1):
        t[i], p[i] = map(int,input().split())
    DFS(1,0)
    print(min)