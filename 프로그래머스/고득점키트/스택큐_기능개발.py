def solution(progresses, speeds):
    stack = []
    answer = []
    for p,s in zip(progresses,speeds):
        if (100-p)%s == 0:
            time = int(((100-p)/s))
        else:
            time = int(((100-p)//s+1))

        if len(stack)==0:
            stack.append(time)

        elif stack[0] < time:
            answer.append([stack[0],len(stack)])
            stack = [time]

        else:
            stack.append(time)

    answer.append([stack[0],len(stack)])
    answer.sort()

    answer = [a[1] for a in answer]

    return answer
