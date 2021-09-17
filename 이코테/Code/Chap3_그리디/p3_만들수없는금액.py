import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-1.그리디/input.txt')

'''
N개의 동전이 주어졌을 때 만들 수 없는 양의 정수 금액 중 최솟값 출력
'''

# 그리디 알고리즘을 많이 접했다면 익숙한 문제
# 아이디어는, 1~target-1금액을 모두 만들 수 있는지를 확인하하는 것이다.

n = int(input())
coins = list(map(int,input().split()))
coins.sort()

target = 1 #첫 타겟 1 설정
for c in coins:
    if target < c: #업데이트 된 타겟이 동전보다 적으면 반복문 탈출
        break
    target += c #업데이트 된 타겟이 동전부다 크다면 타겟 업데이트..

# 이 원리를 어떻게 알아차릴 수 있는 거지?..

print(target)
