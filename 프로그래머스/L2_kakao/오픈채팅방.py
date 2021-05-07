from collections import defaultdict
def solution(record):
    el= {'Enter':'들어왔습니다.' , 'Leave':'나갔습니다.'}
    record = [r.split(' ') for r in record]
    answer = []
    name = defaultdict(str)
    
    # enter / id / name
    temp = []
    for r in record:
        if len(r)==3:
            name[r[1]] = r[2] 
            
        if r[0] in ['Enter','Leave']:
            temp.append([el[r[0]], r[1]])  
               
    for i in range(len(temp)):
        answer.append('님이 '.join([name[temp[i][1]],temp[i][0]]))
    return answer