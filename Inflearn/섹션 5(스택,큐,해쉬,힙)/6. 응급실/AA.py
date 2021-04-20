import sys
from collections import deque
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/6. 응급실/in5.txt","rt")

n,m = map(int,input().split())
a = list(map(int,input().split()))

dan=deque([(idx,val) for idx,val in enumerate(a)])

cnt = 0

while dan:
    check = dan.popleft()
    if check[1] < max(dan, key = lambda x:x[1])[1]:
    #if any(check[1] < x[1] for x in dan)
        dan.append(check)
    else:
        cnt+=1
        if check[0] == m:
            print(cnt)
            break
       

    
    

