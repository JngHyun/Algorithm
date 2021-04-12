import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/10. 동전교환/in5.txt')

N = int(input())
coins = list(map(int,input().split()))
M = int(input())

dy = [100]*(M+1)
dy[0] = 0
for i in range(1,M+1):
    for coin in coins:
        dy[i] = min(dy[i-coin]+1,dy[i])

print(dy[-1])

