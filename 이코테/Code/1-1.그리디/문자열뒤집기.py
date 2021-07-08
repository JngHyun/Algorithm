import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-1.그리디/input.txt')

nums = input()

cnt_0 = 0
cnt_1 = 0

if nums[0]=='0':cnt_0+=1
elif nums[0]=='1':cnt_1+=1

for i in range(1,len(nums)):
    if nums[i]=='0' and nums[i-1] =='1':
        cnt_0+=1
    if nums[i]=='1' and nums[i-1] =='0':
        cnt_1+=1

print(min(cnt_0,cnt_1))