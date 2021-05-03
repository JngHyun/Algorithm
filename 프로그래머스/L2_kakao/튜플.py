from collections import Counter
import re
def solution(s):
    s = s[1:-1].split('},{')
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]
    s = [list(map(int,num.split(','))) for num in s]
    s = sorted(s,key= lambda x: len(x))

    answer = []
    check = set()
    for i in s:
        for num in i:
            if len(answer) ==0:
                answer.append(num) 
            elif len(answer)>0 and num not in check:
                answer.append(num)
        check.update(set(i))
    return answer
