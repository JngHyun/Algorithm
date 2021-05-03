import re
from itertools import permutations

#eval : string expression 계산

def solution(expression):
    answer= 0
    op = set(re.compile('\D').findall(expression))
    order = permutations(op) #operators 조합찾기

    for ops in order:
        temp = re.compile('(\D)').split(expression) #expression to list
        for o in ops:
            while o in temp:
                idx=temp.index(o) #상위순위 operator index 뽑기
                temp = temp[:idx-1]+[str(eval(''.join(temp[idx-1:idx+2])))]+temp[idx+2:] #우선순위부터 계산

        answer=max(answer,abs(int(temp[0])))
    return answer
