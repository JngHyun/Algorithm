import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/5. 최대 선 연결하기/in5.txt')

n = int(input())
num = list(map(int,input().split()))
num.insert(0,0)
left = [0]*(n+1)
left[1]=1
res = 0
for i in range(1,n+1):
    max = 0
    for j in range(1,i):
        if num[j]<num[i] and left[j]>max:
            max = left[j]
        left[i] = max+1
    if left[i] > res:
        res=left[i]

print(res)
    

