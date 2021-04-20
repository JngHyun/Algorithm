# 문제를 풀 때 아주 작은 문제로 바꿔 점점 키워나가 결국 실제 문제를 해결하는 것 
### 1,2m 로 네트워크 선을 자르려고 한다, 자를 수 있는 경우의 수?
# dy[1] = 1
# dy[2] = 2
# dy[3] = dy[2] + dy[1] (2), dy[2] + dy[1] (1) = 2+1 = 3
# dy[4] = dy[3] + dy[1] (3), dy[2] + dy[2] (2) = 3+2 = 5
# ...
# dy[n] = dy[n-1] + dy[n-2]
import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/1, 2. 네트워크 선 자르기/in1.txt')
n = int(input())
dy = [0] *(n+1)
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[n])