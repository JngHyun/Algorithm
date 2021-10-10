def solution(s):
    words = s.lower().split(' ')
    res = []
    for word in words:
        word = list(word)
        for i in range(0,len(word),2):
            word[i] = word[i].upper()
        temp = ''.join(word)
        res.append(temp)
    answer = ' '.join(res)
    return answer