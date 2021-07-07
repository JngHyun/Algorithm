import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-1.그리디/input.txt')

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

######내 풀이########
start = time.time()

data.sort()

sum = 0
l1 = data[-1]
l2 = data[-2]

if l1 == l2:
    sum = l1*m
# 이 부분에서 굳이 cnt 를 쓰지 않고 M을 줄여나가며 풀 수 있음.
else:
    cnt = 0
    while True:
        cnt+=1
        if cnt > m: break
        if cnt % k == 0:
            sum+=l2       
        else:
            sum+=l1
        
print(sum)

end = time.time()
print(f'내가 푼 문제 걸린 시간 : {end-start}')

####### 모범 답안 ######
start = time.time()

data.sort()

first = data[-1]
second = data[-2]

#반복되는 문자열의 길이 : k+1
#반복되는 문자열의 큰 수 반복횟수
    # 1. 나누어 떨어질 때 : m//(k+1)*k
    # 2. 나누어 떨어지지 않을 때 : m//(k+1)*k + (m%(k+1))
count = m//(k+1)*k
count += m%(k+1)

result = 0
result += count * first
result += (m-count)*second

print(result)

end = time.time()
print(f'모범답안 걸린 시간 : {end-start}')