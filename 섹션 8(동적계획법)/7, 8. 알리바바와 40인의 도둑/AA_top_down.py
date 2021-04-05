import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/7, 8. 알리바바와 40인의 도둑/in1.txt')

def DFS(x,y):
    if dy[x][y] > 0: # memoization cut edge
        return dy[x][y]
    if x ==0 and y ==0: # 재귀의 종료 지점 = 출발지점
        return board[0][0] # 첫번째 돌의 에너지 비용
    else:
        if y==0: #맨 왼쪽 줄 / 위로만 호출
            dy[x][y] =  DFS(x-1,y) + board[x][y]
        elif x==0: #맨 위쪽 줄 / 왼쪽으로만 호출
            dy[x][y] = DFS(x,y-1) + board[x][y]
        else: #나머지 줄 위, 왼쪽 중 작은 값 호출
            dy[x][y] =  min(DFS(x-1,y), DFS(x,y-1)) + board[x][y]
        return dy[x][y]
if __name__=='__main__':
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)] # top down memoization을 위한 dinamic matix
    print(DFS(n-1,n-1))

