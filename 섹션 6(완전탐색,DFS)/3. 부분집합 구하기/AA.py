import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6/3. 부분집합 구하기/in2.txt','r')


def DFS(x):
    if x == n+1:      
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=' ')
        print()
    else:
        ch[x] = 1 #사용한다
        DFS(x+1)
        ch[x] = 0 #사용하지 않는다
        DFS(x+1)

if __name__ =="__main__":
    n = int(input())
    ch = [0]*(n+1) # 상태 확인용 
    DFS(1)
