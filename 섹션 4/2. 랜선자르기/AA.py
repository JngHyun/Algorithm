import sys
sys.stdin = open("input.txt","rt")

# 답이 범위 내에서 유효한지에 대해 체크할 때 이분검색을 사용할 수 있다.
k, n =map(int, input().split())

num = []
for i in range(k):
    tmp = int(input())
    num.append(tmp)
    max_num = max(num)

def Count(len):
    sum=0
    for x in num:
        sum+=(x//len)
    return sum

lt = 1
rt = max_num
 
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid-1

print(res)