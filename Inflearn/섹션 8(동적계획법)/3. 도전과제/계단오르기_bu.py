
import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/3. 도전과제/in1.txt')

#bottop-up 방식이 원래 동적계획법
#top-down 방식은 일반 재귀와 같다.

#bottop-up
n = int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2

for i in range(3,n+1):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n])
