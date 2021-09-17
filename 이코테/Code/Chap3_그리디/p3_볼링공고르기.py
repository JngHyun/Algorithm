import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap3_그리디/input.txt')

'''
A.B 두 사람이 볼링을 치고 있다. 서로 무게가 다른 볼링공을 고르려 함
볼링공 : N 개 ( 1 ~  N )
볼링공 무게 : 1 ~ M (같은 것 있을 수 있음)

두 사람이 볼링공을 고르는 경우의 수를 구하시오
'''
start = time.time()
from itertools import combinations
N,M = input().split()
ball = list(map(int,input().split()))

ball_comb = list(combinations(ball,2))
ans=len([x for x in ball_comb if x[0]!=x[1]])

print(ans)

end = time.time()
print(f'내 풀이 걸린 시간 : {end-start}')


#### 모범답안 #####

sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap3_그리디/input.txt')
start = time.time()
n,m = map(int,input().split())
ball = list(map(int,input().split()))

# 1부터 10까지 넣을 리스트
array = [0]*11


for x in ball:
    # 공 무게 별 갯수 
    array[x] += 1

result = 0
#공 무게가 적은 것 부터 A가 선택 했을 때 B가 선택할 수 있는 경우의 수 구하기
for i in range(1,m+1):
    n -= array[i] # 선택한 무게 뺀 나머지
    result += array[i]*n #선택한 무게 * 선택한 무게 뺀 나머지

end = time.time()
print(f'모범답안 걸린 시간 : {end-start}')

