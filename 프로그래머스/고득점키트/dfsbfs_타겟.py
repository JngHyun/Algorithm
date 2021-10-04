def solution(numbers,target):
    answer = 0
    stack = [[numbers[0],0],[-numbers[0],0]]
    n = len(numbers)

    while stack:
        temp,idx = stack.pop()
        idx += 1
        if idx < n:
            stack.append([temp+numbers[idx],idx])
            stack.append([temp-numbers[idx],idx])
        else:
            if temp == target:
                answer += 1
                
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)