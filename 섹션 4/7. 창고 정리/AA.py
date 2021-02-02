import sys
sys.stdin = open("input.txt","rt")

L = int(input())
box = list(map(int, input().split()))
M = int(input())

box.sort(reverse=True)

for _ in range(M):
    box[0] = box[0]-1
    box[-1] = box[-1] + 1

    if box[0]<box[1] or box[-1]>box[-2]:
        box.sort(reverse=True)

print(box[0] - box[-1])