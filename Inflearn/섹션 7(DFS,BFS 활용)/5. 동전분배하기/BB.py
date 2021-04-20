import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/5. 동전분배하기/in5.txt')

def DFS(L):
    global res
    if L == n:
        cha = max(money)-min(money)
        if cha<res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res = cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L] #백해줄 때 준 돈만큼 빼주어야 함


if __name__=='__main__':
    n = int(input())
    coin = []
    money = [0]*3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
    
    