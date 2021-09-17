import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap3_그리디/input.txt')

# 이해안됨
import heapq
def solution(food_times, k):
    if sum(food_times) <=k:
        return -1
    
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value = 0 # 먹기위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous)*length)<= k:
        now = heapq.heappop(q)[0] #현재 시간
        sum_value += (now-previous)*length # 먹기위해 사용된 시간
        length -= 1 #음식하나 줄이기
        previous = now #먹기위해 사용된 시간 바꾸기
        
    result = sorted(q,key=lambda x:x[1])
    return result[(k-sum_value) % length][1]


#내 풀이 - 런타임 에러 / 효율성 0점 ..

'''
def solution(food_times, k):
    if sum(food_times )<=k:
        answer = -1
    else:
        food_cnt = len(food_times)
        step = [x for x in range(food_cnt)] * (2 * 10^13//food_cnt)

        i = 0
        for idx,s in enumerate(step):
            if food_times[s] != 0:
                food_times[s] -= 1
                i += 1
            else:
                pass

            if i == k:
                for j in range(1,food_cnt+1):
                    if food_times[step[idx+j]] != 0:
                        answer = step[idx+j]+1
                        break
                else:
                    answer = -1

    return answer
'''
