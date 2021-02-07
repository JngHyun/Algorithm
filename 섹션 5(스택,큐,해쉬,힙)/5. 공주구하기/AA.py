import sys
from collections import deque
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/5. 공주구하기/in5.txt","rt")

n,k = map(int,input().split())

a = deque([i+1 for i in range(n)])

while len(a)>1:
    a.rotate(-k+1)
    a.popleft()

print(a[0])