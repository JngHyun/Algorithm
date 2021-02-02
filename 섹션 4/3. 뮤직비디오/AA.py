import sys
sys.stdin = open("input.txt","rt")

n , m = map(int, input().split())
a = list(map(int, input().split()))


lt = 1
rt = sum(a)
maxx = max(a)

def Count(cap):
    sum = 0
    cnt = 1
    for x in a:
        if sum+x > cap:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


while lt<=rt:
    mid = (lt+rt)//2
    
    if mid > maxx and Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)
    


