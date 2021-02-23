import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/3. 양팔저울/in5.txt')

def DFS(L,sum):
    if L==k:
        if 0<sum<=s: #음수는 보지 않아도 대칭구조로 나중에 체크 됨
            res.add(sum) #set 자료구조 .add
    else:
        DFS(L+1, sum + chu[L])
        DFS(L+1, sum - chu[L])
        DFS(L+1, sum)

if __name__ == '__main__':
    k = int(input())
    chu = list(map(int,input().split()))
    s = sum(chu)
    res = set()
    DFS(0,0)
    print(s-len(set(res)))
