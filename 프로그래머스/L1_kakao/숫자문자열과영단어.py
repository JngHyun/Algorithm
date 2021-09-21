def solution(s):
    data = ['zero','one','two','three','four','five','six','seven','eight','nine']
    if s.isdigit():
        return int(s)
    else:
        temp = ''
        result = ''
        for i in s:
            if i.isalpha():
                temp+=i
                try:
                    idx = data.index(temp)
                    result += str(idx)
                    temp = ''     
                except:
                    pass
            else:
                result += i
        return int(result)



def solution(s):
    data = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx,value in enumerate(data):
        s=s.replace(value,str(idx))
    
    return int(s)