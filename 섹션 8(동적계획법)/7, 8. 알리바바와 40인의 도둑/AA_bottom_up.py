import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/7, 8. 알리바바와 40인의 도둑/in1.txt')

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = board[0][0]

#맨 윗줄, 맨 왼쪽줄은 한 방향으로 만 움직일 수 있기 때문에 누적해서 만들어줌
for i in range(n):
    dy[i][0] = dy[i-1][0] + board[i][0]
    dy[0][i] = dy[0][i-1] + board[0][i] 
# 나머지는 위쪽, 왼쪽중 누적 길이가 적은 값을 가져와 dy 에 기록한다.
for i in range(1,n):
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j],dy[i][j-1]) + board[i][j]

print(dy[n-1][n-1])


