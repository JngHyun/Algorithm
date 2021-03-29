import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/3. 도전과제/in1.txt')
#돌다리 건너기는 돌의 갯수 + 1 이 도착지점인 것을 고려해주어야 함

n = int(input())
dy = [0]*(n+2)

dy[1]=1
dy[2]=2

for i in range(3, n+2):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n+1])