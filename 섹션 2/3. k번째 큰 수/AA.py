import sys
#sys.stdin = open("input.txt","rt")

from itertools import combinations
n,k = map(int,input().split())
N = list(map(int,input().split()))
comb= list(combinations(N,3))
print(sorted(set([sum(i) for i in comb]),reverse=True)[k-1])
