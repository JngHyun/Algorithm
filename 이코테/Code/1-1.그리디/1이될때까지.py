# 항상 1을 뺴는 것보다 2이상의 숫자로 나누는 것이 n의 크기를 더 많이 줄일 수 있다.

n,k = map(int,input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 순간까지 빼기
    target = (n//k)*k
    result += (n-target) #1을 빼는 연산 횟수 한번에 더하기
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    result += 1
    n//=k

#남은 수에 대해 1을 빼는 연산 한번에 하기
result += (n-1)
print(result)

# 코드가 빨리 실행 될 수 있도록 함
# n, k가 백억, 천억이 되어도 로그시간 복잡도

