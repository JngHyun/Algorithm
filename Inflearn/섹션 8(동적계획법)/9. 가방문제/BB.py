import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/9. 가방문제/in3.txt')

if __name__=="__main__":
    n,m = map(int,input().split())
    dy = [0] * (m+1)
    for i in range(n):
        w,v = map(int,input().split())
        for j in range(w,m+1): #w부터 fo문이 돌도록함
            dy[j] = max(dy[j],dy[j-w]+v)

