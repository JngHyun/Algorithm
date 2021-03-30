import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/4. 최대부분증가수열/in5.txt')

n=int(input())
nums = list(map(int,input().split()))
nums.insert(0,0)
dy = [0]*(n+1)

dy[1] = 1

for i in range(1,n+1):
    m = 0
    for j in range(i):
        if nums[j]<nums[i]:
            m = max(m,dy[j])
    dy[i] = m+1

print(max(dy))
                