import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
scores = list(map(int, input().split()))

#avg = round(sum(scores)/n)
avg = int(sum(scores)/n+0.5)

min = 2147000000
for idx, x in enumerate(scores):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score: # score>=x 로 바꾸면 맨 뒤에 학생이 저장됨
            score = x
            res = idx+1

print(avg,res)  


