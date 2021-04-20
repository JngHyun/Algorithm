import sys
import heapq
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/11. 최대힙/in1.txt","rt")

heap = []

while True:
    a = int(input())

    if a == 0 and len(heap) != 0:
        # 출력을 해야하는 상황에는 heappo으로 출력된 튜플의 1번 index 값을 출력한다.
        print(heapq.heappop(heap)[1])
    elif a == 0 and len(heap) == 0:
        print(-1)
    elif a == -1:
        break
    else:
        # 튜플을 힙의 원소로 추가하면 맨앞에 있는 값을 기준으로 최소 힙이 구성된다.
        # 따라서 입력 원소의 음수값(입력 원소의 최대값)의 최소를 기준으로 힙이 구성된다.
        heapq.heappush(heap,(-a,a))

    #걍 음수로 해도 됨
     

