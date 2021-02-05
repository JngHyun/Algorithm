import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6/4. 합이 같은 부분집합/in5.txt','r')

#부분집합 DFS와 동일한 코드
def DFS(x):
    if x == n:
        sum1 = sum([x for (x,v) in zip(num,check) if v])
        sum2 = sum([x for (x,v) in zip(num,check) if not v])
        if sum1 == sum2:
            print('YES')
            sys.exit(0) #if문 탈출을 위함

    else:
        check[x] = True
        DFS(x+1)
        check[x] = False
        DFS(x+1)

if __name__ =='__main__':
    n = int(input())
    check = [0] * n
    num = list(map(int,input().split()))
    DFS(0)
    print('NO')

    