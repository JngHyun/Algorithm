import sys
from collections import deque
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/5. 공주구하기/in1.txt","rt")

n,k = map(int,input().split())

a = deque(list(range(1,n+1)))

while a:
    for _ in range(k-1):
        tmp = a.popleft()
        a.append(tmp)
    a.popleft()
    if len(a)==1:
        print(a[0])
        a.popleft()
