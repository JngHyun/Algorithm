def solution(new_id):
    answer = ''
    used = []
    used += [i for i in range(ord('a'),ord('z')+1)]
    used += [i for i in range(ord('0'),ord('9')+1)]
    used += [ord('-'),ord('_'),ord('.')]
    
    new_id = new_id.lower()

    for a in new_id:
        if ord(a) in used:
            answer+=a
             
    temp=answer[0]
    for i in range(1,len(answer)):
        if answer[i]=='.' and temp[-1] == '.':
            temp+=''
        else: 
            temp+=answer[i]
    answer = temp

    
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer)!= 0 and answer[-1] =='.':
         answer = answer[:-1]
    
    if len(answer) ==0:
        answer = 'a'
    
    if len(answer) >=16:
        answer = answer[:15]
    
    if len(answer)!= 0 and answer[-1] =='.':
         answer = answer[:-1]
        
    if len(answer)<=2:
        temp = answer[-1]
        while len(answer)!=3:
            answer+=temp
            
    return answer