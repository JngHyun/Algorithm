def solution(answers):
    answer = []

    
    s1 = [1,2,3,4,5] 
    s2 = [2,1,2,3,2,4,2,5] 
    s3 = [3,3,1,1,2,2,4,4,5,5]

    sc1_score=0;sc2_score=0;sc3_score=0
    
    for i,a in enumerate(answers):
        if a == s1[i%len(s1)]: sc1_score+=1
        if a == s2[i%len(s2)]: sc2_score+=1
        if a == s3[i%len(s3)]: sc3_score+=1
            
    answer = [sc1_score,sc2_score,sc3_score]
    answer = [i+1 for i,x in enumerate(answer) if x == max(answer)]
    
    return answer