### 출제 경향
1. Greedy
2. 구현
3. DFS/BFS

    > 카카오 : 구현, 문자열 처리 문제 많이 풀어보기   

### 알고리즘 성능 평가
- 복잡도 : 메모리가 얼마나 필요한지   
- 빅오 표기법   
    O(1)   
    O(logN)   
    O(N)   
    O(NlogN)   
    O(N^2)   
    O(N^3)   
    O(2^n)   

- 연산횟수가 5억이 넘어가는 경우 Python 5~15초 가량 소요 (시간제한은 통상 1~5초)
- PyPy가 python보다 빠르니 PyPy로 제출해보기

    > N < 500 : O(N^3)   
    > N < 2000 : O(N^2)   
    > N < 100,000 : O(NlogN)   
    > N < 10,000,000 : O(N)   

### 알고리즘 문제 해결 과정
1. 지문 읽기 및 컴퓨터적 사고
2. **요구사항(복잡도)분석**
3. 문제해결을 위한 아이디어 찾기
4. 소스코드 설계 및 코딩

    수행 시간 측정 코드
    ```ruby
    import time
    start_time = time.time()
    end_time = time.time()
    print("time" , end_time - start_time)
    ```

## 자료형
### 실수형
* round 함수로 실수형 표현 보정

### 리스트
* 리스트 컴프리헨션   
    ```ruby 
    # 2의배수 출력
    [i for i in range(20) if i%2==0]

    # 2차원 리스트 초기화
    # 좋은 예시
    array = [[0] * m for _ in range(n)]
    # 나쁜 예시 - 내부 리스트가 모두 같은 객체로 인식 됨
    array = [[0] * m] * n
    ```

* method
    ```ruby 
    Name.append()   
    Name.sort(),Name.sort(reverse=True)# O(NlogN)
    Name.reverse()#O(N)    
    insert(index, val)   
    Name.count(val)   
    Name.remove(val)   
    ```

### 문자열
* 문자열은 원소할당을 지원하지 않음(변경불가 객체)

### 튜플
*한번 선언된 값 변경 불가*   
* 서로다른 성질의 데이터 묶어서 관리할 때
* 데이터의 나열을 Hashing 키 값으로 사용해야 할 때
* 메모리를 효율적으로 사용할 때

### 사전
* 변경 불가능한 자료형을 키로 사용
* 해쉬 테이블 , **데이터 조회 및 처리 O(1)**
```ruby 
list(Name.keys())
list(Name.values())
```

### 집합
*중복 x, 순서 x*   
* **데이터 조회 및 처리 O(1)**   
* 인덱싱으로 접근 불가   

```ruby
# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)

Name.add(vale)
Name.update([values])
Name.remove(value)
```

## 입출력 양식
```ruby
list(map(int,input().split()))
a,b,c = map(int,input().split())

# 사용자로부터 문자열 입력 받기
data = sys.stdin.readline().rstrip()

# 줄바꿈 발생 x print
for i in range(n):
    print(i, end=' ')
```

## 조건문과 반복문

* 파이썬에서 가능한 논리식 표현
    ```ruby
    x = 15
    if 0<x<20:
        print("x는 0이상 20이하 수이다")
    ```
* 조건문 pass 
* 반복문 continue
* 반복문 break(탈출!)

## 함수와 람다 표현식
* 내장 함수
* 사용자 정의 함수

### 글로벌 키워드
```ruby
a=0
def func():
    global a
    a+=1

for i in range(10):
    func()
print(a) # a=10

# 리스트는 전역변수로 많이 사용
array = [1,2,3]
def func():
    global array
    array = [3,4,5]
    array.append(6)
    
func() 
print(array) #[1,2,3,6]
```

### 람다 표현식

```ruby
print((lambda a,b:a+b)(3,7))
```

내장 함수에 사용   
```ruby
array = [('홍길동',50),('이순신',32),('아무개',74)]
# 나이순으로 정렬
sorted(array,key=lambda x: x[1])
```
여러 개의 리스트에 사용
```ruby
list1 = [1,2,3]
list2 = [3,4,5]

result = map(lambda a,b : a+b,list1,list2)
# 각 인덱스 별로 합 구함
```

## 내장함수
* itertools : 순열과 조합 
* heapq : 우선순위 큐
* bisect : 이진탐색
* colection : deque, Counter
* math

자주 사용되는 내장 함수
```ruby
sum()
min()
max()

eval()
# 문자열 수식 계산
result = eval('(3+5)*7')
print(result) # 56

sorted()
sorted(array, key=lambda x:x[1], reverse = True)
```

순열과 조합
```ruby
from itertools import permutations # 순열
from itertools import combinations # 조합
data = [1,2,3]

list(permutations(data,2))
list(combinations(data,2))
```

Counter   
반복 가능한 객체에서 내부 원소의 갯수를 구할 때 사용
```ruby
from collections import Counter

Counter(list)
```

최대 공약수, 최소 공배수
```ruby
import math

def lcm(a,b):
    return a*b // math.gcd(a,b)

# gcd 최대공약수 계산
# lcm 최소공배수 계산
```





















