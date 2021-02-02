import sys
#sys.stdin = open("input.txt","rt")

n = int(input())

for i in range(n):
    res =0
    strings = str(input())
    strings = strings.lower()
    
    n=len(strings)
    
    for j in range(n//2):
        if strings[j] != strings[n-1-j]:
            res+=1
            print("#%d NO"%(i+1))
            break 
    
    if res==0:
        print("#%d YES"%(i+1))




    
