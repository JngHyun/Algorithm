import sys
from collections import deque
sys.stdin = open("input.txt","rt")

n ,m = map(int,input().split())
people = list(map(int,input().split()))
people.sort()
cnt = 0

# list 에서는 앞자리 pop 하면 뒤에 element들이 앞으로 움직이기 대문에 비효율적
# collections deque 는 앞뒤로 원소를 넣다 뺐다 할 수 있음.
# .popleft = .pop(0)
'''
people = deque(people)

while people:
    if len(people) ==1:
        cnt +=1
        break
    if people[0]+people[-1]>m:
        people.pop()
        cnt +=1
    else:
        people.popleft()
        people.pop()
        cnt +=1

print(cnt)
'''

while people:
    if len(people) == 1:
        cnt+=1
        break
    if people[0] + people[-1] > m:
        #가장 무거운 사람만 혼자타고 탈출
        people.pop()
        cnt += 1
    else:
        # 둘이 탈출
        people.pop(0)
        people.pop()
        cnt +=1

print(cnt)