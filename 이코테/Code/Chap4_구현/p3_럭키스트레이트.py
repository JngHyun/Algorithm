import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap4_구현/input.txt')

'''
현재 점수가 주어졌을 때, 점수 중간을 나눠 왼쪽부분과 오른쪽부분의 합을 비교
그 합이 같으면 LUCKY 출력 다르면 READY 출력 
'''

data = input()
length = len(data)
mid = length//2

left = sum(list(map(int,data[:mid])))
right = sum(list(map(int,data[mid:])))

if left==right:
    print('LUCKY')
else:
    print('READY')