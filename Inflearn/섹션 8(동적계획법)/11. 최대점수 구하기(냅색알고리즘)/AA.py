import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/11. 최대점수 구하기(냅색알고리즘)/in2.txt')

n,m = map(int,input().split())

#(score,time)
test = [tuple(map(int,input().split())) for _ in range(n)]
dy = [0]*(m+1)

for score,time in test:
    for i in range(m,time-1,-1):
        dy[i] = max(dy[i],dy[i-time] + score)
print(max(dy))


