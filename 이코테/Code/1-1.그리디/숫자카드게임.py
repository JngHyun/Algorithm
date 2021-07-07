import sys
import time
######내 풀이########
start = time.time()
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-1.그리디/input.txt')

n,m = map(int,input().split())
max = 0
for i in range(n):
    data = list(map(int,input().split()))
    min = 10001
    for j in range(m):
        if data[j]<min:
            min = data[j]
    if min>max:
        max = min        
print(max)
end = time.time()
print(f'내가 푼 문제 걸린 시간 : {end-start}')

# list min,max function 사용 가능

####### 모범 답안 ######

start = time.time()
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-1.그리디/input.txt')

n,m = map(int,input().split())
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_val = min(data)
    result = max(min_val,result)
print(result)

end = time.time()
print(f'모범답안 걸린 시간 : {end-start}')