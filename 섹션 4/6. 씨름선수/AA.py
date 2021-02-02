import sys
sys.stdin = open("input.txt","rt")

n = int(input())

s = []
for _ in range(n):
    s.append(list(map(int,input().split())))

s.sort(reverse=True)
cnt = 0
largest = 0

for height, weight in s:
    if weight > largest :
        cnt +=1
        largest = weight

print(cnt)
