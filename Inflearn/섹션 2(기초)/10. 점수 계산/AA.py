import sys
sys.stdin = open("input.txt","rt")

n=int(input())
nums = list(map(int,input().split()))
sum=0
temp=0
for i in range(n):
    if nums[i] ==0:
        temp = 0
    else:
        temp+=1
        sum+=temp

print(sum)



