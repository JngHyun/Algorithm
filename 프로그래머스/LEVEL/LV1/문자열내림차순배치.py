import re
def solution(s):
    answer = ''
    l = re.findall("[a-z]",s)
    u = re.findall("[A-Z]",s)
    l.sort(reverse=True)
    u.sort(reverse=True)
    total = l+u
    for t in total:
        answer += t
    return answer


# sorted는 문자열 배열도 순서 정렬해줌 
def solution(s):
    return ''.join(sorted(s, reverse=True))
