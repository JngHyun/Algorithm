import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
num = list(map(int,input().split()))

num.sort()

lt = 0
rt = n -1

while lt<=rt:
    mid = (lt+rt)//2
    if num[mid] == m:
        print(mid+1)
        break
    elif num[mid] > m:
        rt = mid-1
    elif num[mid] < m:
        lt = mid+1


