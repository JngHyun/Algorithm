# DFS(7) : 7m 짜리 네트워크를 자르는 방법을 리턴받는 함수
#           D(7)
#           /  \
#         D(6) D(5) : 끝에가 각각 1, 2일때
#         / \
#       D(5) D(4)
#       / \
#     D(4) D(3)
#     /  \
#   D(3) + D(2)
#   /  \
#D(2) + D(1)
# 쭉 위로 더함
# dy = [] 에 이미 구해진 값 넣어서 재귀 돌 때 사용 : 메모이제이션
import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/1, 2. 네트워크 선 자르기/in5.txt')

def DFS(len):
    # cut : 가지 뻗지말고 있는 값은 있는거 바로 뽑기
    if dy[len]>0:
        return dy[len]
    #메모이제이션
    if len == 1 or len ==2:
        return len
    else:
        dy[len] = DFS(len-1)+DFS(len-2)      
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy=[0]*(n+1)
    print(DFS(n))