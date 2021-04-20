import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/1. 최대점수 구하기/in5.txt')

# 제공된 문제 부분집합를 구하기 
#      
# 1   o /\ x
# 2 o /\ x 
# 3   o/\x
# 이런식으로 내려가서 부분집합 구하기


def DFS(L,sum,time):
    global res
    if time > m:
        return
    if L == n: #부분집합 하나 완성
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)

if __name__ =='__main__':
    n,m = map(int,input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a,b = map(int,input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0,0,0)
    print(max)