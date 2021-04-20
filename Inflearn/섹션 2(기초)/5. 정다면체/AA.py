import sys
#sys.stdin = open("input.txt","rt")

from collections import Counter
n,m = map(int, input().split())
n = list(range(1,n+1))
m = list(range(1,m+1))

sum = []
for i in n:
    for j in m:
       sum.append(i+j)

sum_cnt = dict(Counter(sum))
max = max(sum_cnt.values())
maxes = sorted([k for k,v in sum_cnt.items() if v == max])

for i in maxes:
    print(i, end=" ")