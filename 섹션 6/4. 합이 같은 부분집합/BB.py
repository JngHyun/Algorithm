import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6/4. 합이 같은 부분집합/in5.txt','r')

def DFS(L,sum):
    if sum > total//2: #시간복잡도를 줄이기 위해 추가 / total//2보다 큰 경우 함수를 더 진행할 이유가 없다.
        return
    if L==n:
        if sum==(total-sum): #내가 만든 부분집합의 합을 전체에서 뺀 것과 같아야 함.
            print('YES')
            sys.exit(0) #프로그램 전체를 종료시킴
    else:
        DFS(L+1,sum+a[L]) #왼쪽노드(사용하는 부분)
        DFS(L+1,sum) #오른족노드(사용하지 않는 부분)

if __name__=='__main__':
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print('NO')