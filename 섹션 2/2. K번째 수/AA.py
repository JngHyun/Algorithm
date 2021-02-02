import sys
#sys.stdin = open("input.txt","rt")

T = int(input())
for i in range(T):
    n,s,e,k = map(int,input().split())
    N = list(map(int,input().split())) #숫자 list로 만들어야함
    N = sorted(N[s-1:e])
    print("#%d %d" %(i+1,N[k-1]))
    
    

