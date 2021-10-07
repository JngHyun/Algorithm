def solution(arr1, arr2):
    answer = []
    for num1,num2 in zip(arr1,arr2):
        answer.append(list(map(sum,zip(num1,num2))))
    return answer
