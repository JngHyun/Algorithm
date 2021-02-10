import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/7. 동전교환/in3.txt')

def DFS(x,sum):
    global res
    if x >= res: # 최소 갯수 보다 많으면 cut
        return
    if sum>m: # 잔돈보다 커지면 cut
        return
    if sum == m: # 잔돈이랑 갯수가 맞으면
        if x<res: #갯수 비교 
            res = x # 더 적은 경우로 update
    else:
        for i in range(n):
            DFS(x+1,sum+coin[i]) # 
    
if __name__ == '__main__':
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())
    res = 2147000000
    coin.sort(reverse=True)
    DFS(0,0)
    print(res)