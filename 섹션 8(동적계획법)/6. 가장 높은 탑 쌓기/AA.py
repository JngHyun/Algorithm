import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/6. 가장 높은 탑 쌓기/in1.txt')

# 밑면, 높이, 무게
n = int(input())
block = [tuple(map(int,input().split())) for _ in range(n)]
block.sort(reverse=True)

res = block[0][1]
dy = [0] * n # 최대 높이를 누적 할 list
dy[0] = block[0][1]

for i in range(n):
    max_h=0
    for j in range(n-1,-1,-1):
        if block[j][2]>block[i][2] and dy[j]>max_h:
            max_h = dy[j]
    dy[i] = max_h + block[i][1]

    res = max(res,dy[i])
print(res)
