import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/9. 가방문제/in3.txt')

N,W = map(int,input().split())
x = [tuple(map(int,input().split())) for _ in range(N)]

# dy[j] : 가방에 들어간 j무게 보석의 최대 가치
dy = [0] * (W+1)

for i in range(N): #가방에 보석을 하나씩 넣어봄
    w,v = x[i][0],x[i][1] #보석의 무게, 보석의 가치
    for j in range(W+1): # 들어갈 수 있는 보석의 총 무게    
        if j>=w and dy[j-w] + v >= dy[j]:
            dy[j] = dy[j-w] + v
    
print(max(dy))


