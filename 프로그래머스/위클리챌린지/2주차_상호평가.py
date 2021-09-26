def solution(scores):
    answer = ''
    
    # list traspose
    #scores = [[s[i] for s in scores] for i in range(len(scores))]
    scores = [list(x) for x in zip(*scores)]
    #scores = list(map(list,zip(*scores)))
    
    for idx, score in enumerate(scores):
        min_s = min(score)
        max_s = max(score)
        total_s = sum(score)
        student = len(score)
        my_s = score[idx]
        
        if my_s == min_s or my_s == max_s: 
            if score.count(my_s)==1:
                total_s -= my_s
                student -= 1

        s = total_s / student
    
        if   s>=90: answer+='A'
        elif s>=80: answer+='B'
        elif s>=70: answer+='C'
        elif s>=50: answer+='D'
        else: answer+='F'
        
    return answer