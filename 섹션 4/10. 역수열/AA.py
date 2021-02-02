import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
seq = [0] * n
print(a)

for idx,num in enumerate(a):
    cnt = 0
    for i in range(n):
        if seq[i] == 0:
            cnt += 1
        if cnt == num+1:
            break
    seq[i] = idx + 1 

for x in seq:
    print(x,end=" ")

'''
for i in range(n):
    for j in range(n):
        # 자기 앞에 빈공간을 확보하고 자리에도 아무도 없다.
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            # 빈공간을 몇개 확보했는지 확인해 주기 위해 a[i] 에서 하나씩 뺀다.
            a[i] -= 1
'''