import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-2.구현/input.txt')


dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int,input().split())
A,B,d = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]
data[A][B]=1

result = 0
while True:
    check = 0
    for i in range(3):
        next = d-1
        if d-1<0:
            next = 3
        
        cx = A + dx[next]
        cy = B + dy[next]

        if data[cx][cy] == 0:
            A = cx
            B = cy
            d = next
            data[A][B] = 1
            result += 1
            break
        else:
            d = next
            check += 1       

    if check ==3:    
        cx = A
        cy = B+1

        if data[cx][cy]==1:
            break
        else:
            A = cx
            B = cy
            d = next
            result +=1

print(result+1)

    
    


