def solution(s):
    s = s.lower()
    p = 0;y=0
    for i in s:
        if i =='p':
            p+=1
        if i =='y':
            y+=1

    if p == y:
        answer = True
    else:
        answer = False
       
    return answer

#count함수!!!!
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')