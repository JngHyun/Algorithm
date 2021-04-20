import sys
sys.stdin = open("input.txt","rt")

n =int(input())

h = []
for _ in range(n):
    h.append(list(map(int, input().split())))

# 회의가 끝나는 시간을 기준으로 정렬해야 함
# 키 지정하지 않으면 앞의 열 기준으로 정렬한다
h.sort(key = lambda x : (x[1], x[0]))

et =0
cnt = 0
for s,e in h:
    if s>=et:
        et = e
        cnt += 1

# for i in range(n):
#     cnt = 1
#     end = h[i][1]
#     s=i
#     for j in range(s+1,n):
#         if h[j][0] >= end:
#             cnt += 1
#             end = h[j][1]
#             s = j
#     if cnt >= max:
#         max=cnt


print(cnt)