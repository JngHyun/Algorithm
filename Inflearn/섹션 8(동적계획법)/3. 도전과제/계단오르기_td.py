#top-down
import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/3. 도전과제/in1.txt')

def DFS(x):
    if dy[x]>0:
        return dy[x]
    if x==1 or x==2:
        return x
    else:
        dy[x] = DFS(x-1)+DFS(x-2)
        return dy[x]


if __name__ =='__main__':
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))