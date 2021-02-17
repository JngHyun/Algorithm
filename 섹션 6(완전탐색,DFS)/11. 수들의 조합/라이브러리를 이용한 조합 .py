import sys
import itertools as it
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/11. 수들의 조합/in1.txt')
n,k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
cnt = 0

for x in it.combinations(a,k): # a 리스트에서 k 개 뽑아 조합 만들기
    if sum(x)%m==0:
        cnt+=1

print(cnt)
