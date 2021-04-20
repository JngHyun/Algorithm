import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/13. 회장뽑기/in3.txt')

n = int(input())
dis = [[100]*(n+1) for _ in range(n+1)] # 회원이 50명 까지 들어오니까 가장 멀리 돌아가도 50이라 100으로 초기값  초기화

for i in range(1,n+1):
    dis[i][i]=0

while True:
    f1 ,f2 = map(int,input().split())
    if f1 == -1 and f2 ==-1:
        break
    dis[f1][f2] = 1
    dis[f2][f1] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+ dis[k][j])

res = [0]*(n+1)
score = 100
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i] = max(res[i],dis[i][j])
    score = min(score,res[i])

out = [] #회장 후보들의 번호 입력
for i in range(1,n+1):
    if res[i] == score:
        out.append(i)

print('%d %d' %(score,len(out)))
print(*out,end=' ')

    


