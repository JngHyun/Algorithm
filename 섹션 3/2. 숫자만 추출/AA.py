import sys
#sys.stdin = open("input.txt","rt")

S = input()

res = 0
cnt = 1
for s in S:
    if s.isdecimal():
        res = res * 10 + int(s)
    
for i in range(1,res//2+1):
    if res%i == 0:
        cnt+=1

print(res)
print(cnt)



    

