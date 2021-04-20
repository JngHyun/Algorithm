import sys
#sys.stdin=open("input.txt","rt")

n,k = map(int, input().split()) # input split 문자 int로 읽고 map
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt+=1
    if cnt ==k:
        print(i)
        break
else:
    print(-1) #for문 break 지나고


