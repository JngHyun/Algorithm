import sys
import heapq as hq
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/10. 최소힙/in3.txt","rt")

heap = []

while True:
    a = int(input())

    if a == 0 and len(heap) != 0:
        print(hq.heappop(heap))
    elif a == 0 and len(heap) == 0:
        print(-1)
    elif a == -1:
        break
    else:
        hq.heappush(heap,a)



