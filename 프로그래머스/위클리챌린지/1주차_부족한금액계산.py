def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(1,count+1):
        sum += price * i

    if sum - money < 0:
        answer = 0
    else:
        answer = sum-money

    return answer

# 파이썬
def solution(price, money, count):
    return max(0,sum([price*i for i in range(1,count+1)]) - money)

