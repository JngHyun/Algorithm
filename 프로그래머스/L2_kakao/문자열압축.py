def solution(s):
    answer = 147000
    n = len(s)
    for i in range(1,n//2+1):
        start = 0
        tok = []
        for _ in range(n//i):
            end = start + i
            tok.append(s[start:end])
            start = end
        tok.append(s[end:])

        temp = [str(tok[0])]
        cnt = 0
        for t in tok:
            if temp[-1] == str(t):
                cnt += 1
                temp.pop(-1)
                temp.append(str(t))
            else:
                if cnt != 1:
                    x = temp.pop(-1)
                    temp.append(str(cnt)+x)
                cnt = 1
                temp.append(str(t))
        temp2 = ''.join(temp)
        answer= min(answer,len(temp2))
    answer = min(answer,len(s))
    return answer
