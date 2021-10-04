def solution(strings, n):
    answer = 0
    string = [[s[n],s] for s in strings]
    string.sort()
    answer = [s[1] for s in string]
    return answer

def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))
