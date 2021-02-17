import sys
import itertools as it
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6(완전탐색,DFS)/9. 수열 추측하기/in1.txt')

n,f = map(int,input().split())
b = [1] * n
cnt = 0

for i in range(1,n):
    b[i] = b[i-1]*(n-i)/i #이항계수
a = list(range(1,n+1))    #수열

'''
# library 를 이용해 입력 list를 이용한 모든 순열 구하기
# tuple 자료로 구해짐
for tmp in it.permutations(a): 
    print(tmp)

# aP3
for tmp in it.permutations(a,3): 
    print(tmp)
'''

for tmp in it.permutations(a): #수열로 순열만들기
    sum=0
    for L,x in enumerate(tmp): #순열과 이항계수의 원소를 곱해주기 위함
        sum += (x*b[L])
    if sum==f:
        for x in tmp:
            print(x,end=' ')
        break # for 문 break