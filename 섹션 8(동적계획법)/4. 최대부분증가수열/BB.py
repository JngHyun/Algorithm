import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/4. 최대부분증가수열/in5.txt')

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

dy = [0]*(n+1)
arr[1]=1
res =0

for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max = dy[j]
    dy[i] = max+1
    if dy[i] > res:
        res = dy[i]

print(res)
