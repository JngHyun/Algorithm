import sys
from collections import deque
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/7. 교육과정 설계/in1.txt","rt")

order = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(order)
    for p in plan:
        if p in dq:
            if p != dq.popleft():
                print('#%d NO'%(i+1))
                break
    else:
        if len(dq)==0:
            print('#%d YES'%(i+1))
        else: 
            print('#%d NO'%(i+1))