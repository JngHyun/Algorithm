import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/8. 사과나무/in2.txt')

n = int(input())
apple = []
for i in range(n):
    apple.append(list(map(int,input().split())))

total = sum(apple[n//2])
for i in range(n//2):
    l = n//2-i
    r = n//2+i
    total += sum(apple[i][l:r+1])
    total += sum(apple[n-1-i][l:r+1])

print(total)