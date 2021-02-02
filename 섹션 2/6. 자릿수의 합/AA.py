import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
nums = list(input().split())

def digit_sum(x):
    max = -276000000
    for num in x:
        sum = 0
        for i in num:
            sum += int(i)
        if sum > max:
            max = sum
            result = num
    return result

print(digit_sum(nums))
