def solution(n):
    flag= [False]*(n+1)

    m = int(n**0.5)
    for i in range(2,m+1):
        if flag[i] == False:
            for j in range(i+i,n+1,i):
                flag[j] == True
    
    answer = [i for i in range(2,n+1) if flag[i] == False]


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
