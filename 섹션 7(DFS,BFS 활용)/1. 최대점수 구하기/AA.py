import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/1. 최대점수 구하기/in5.txt')

def DFS(x,time,tot):
    global max
    if time > m:
        return
    if x == n:
        if tot > max:
            max = tot
    else:
            DFS(x+1,time + L[x][1],tot + L[x][0])
            DFS(x+1,time,tot)

if __name__ =='__main__':
    n,m = map(int,input().split())
    max = -247000000
    L=[]
    for i in range(n):
        a,b = map(int,input().split())
        L.append((a,b))
    DFS(0,0,0)
    print(max)

