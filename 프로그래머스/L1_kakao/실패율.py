def solution(N, stages):
    answer = []
    tot = len(stages)
    for i in range(1,N+1):
        if tot ==0:
            fr = 0
        else:
            sum = stages.count(i)
            fr = sum/tot
        answer.append((i,fr))
        tot -= sum
    answer = sorted(answer, key=lambda t: t[1], reverse=True)   
    answer = [x[0] for x in answer]
    
    return answer