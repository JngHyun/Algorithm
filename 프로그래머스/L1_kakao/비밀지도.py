def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1,arr2):
        temp = ''
        for k in range(n):
            if i%2 ==0 and j%2 ==0:
                temp += ' '
            else:
                temp += '#'
            i = i//2
            j = j//2
        answer.append(temp[::-1])

    return answer


# 좀 더 간단한 방법
# a | b : 비트 연산자 (ex) 1010 | 1001 => 1011 => 11 
# bin(a|b)= bin(11) : 11을 다시 이진수로 == > 1011 
