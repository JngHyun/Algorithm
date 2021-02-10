import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/8. 순열 구하기/in2.txt')

# 중복 조합 문제에서 중복인 경우 뻗지 못하게 cut

def DFS(x,res):
    global cnt
    if x>=m:
        for a in res:
            print(a,end=' ')
        cnt+=1
        print()
        return

    else:
        for i in range(1,n+1):
            if ch[i] == 0: #한번 사용된 경우 출력되지 못하게 중복 cut
                ch[i] = 1 #사용 여부 check 하기  
                res[x] = i
                DFS(x+1,res)
                ch[i]=0 #back하게 되는 경우 사용 여무 check 풀어줌

if __name__ == '__main__':
    n,m = map(int,input().split())
    # n = 3
    # m = 2
    res = [0] * (m)
    ch = [0]*(n+1)
    cnt = 0
    DFS(0,res)
    print(cnt)


