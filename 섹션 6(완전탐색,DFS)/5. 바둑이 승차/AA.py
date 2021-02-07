import sys
sys.stdin=open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/5. 바둑이 승차/in2.txt')

def DFS(x,total,tsum):
    global result
    if total+(all-tsum) < result:
        return
    if total>c:
        return
    if x == n:
        if total > result:
            result = total

    else:
        DFS(x+1,total+dogs[x],tsum+dogs[x])
        DFS(x+1,total,tsum+dogs[x])


if __name__ == '__main__':
    c,n = map(int,input().split())
    total = 0
    dogs = []
    result = -247000000
    for i in range(n):
        dogs.append(int(input()))
    all = sum(dogs)
    DFS(0,0,0)
    print(result)