import sys
sys.stdin=open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/5. 바둑이 승차/in2.txt')

def DFS(x,total,tsum):
    global result
    if total+(all-tsum) < result: #second : 앞으로의 모든 것을 추가해도 result보다 작은경우 더 볼 필요 없음
        return
    if total>c: # first cut
        return
    if x == n:
        if total > result: #최대값 찾기
            result = total
    else: #부분집합 만듬
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