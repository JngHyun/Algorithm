import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/4. 동전바꿔주기/in5.txt')

def DFS(x,sum):
    global cnt
    if sum>t:
        return
    if x==k:
        if sum == t:
            cnt += 1
    else:
        for i in range(n[x]+1):
            DFS(x+1,sum+(p[x]*i))
    

if __name__=='__main__':
    t = int(input())
    k = int(input())
    p = [0]*k
    n = [0]*k

    for i in range(k):
        p[i],n[i] = map(int,input().split())

    cnt = 0 
    
    DFS(0,0)
    print(cnt)
