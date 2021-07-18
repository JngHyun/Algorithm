import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1. 그리디&구현/input.txt')

N = int(input())
data = list(map(int,input().split()))
# 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가 수만 포함해 그룹을 결성하게 된다.
data = sorted(data)

count = 0 ; group = 0
for d in data:
   count +=1
   if count  >= d:
       group +=1
       count = 0
    
print(group)
    
