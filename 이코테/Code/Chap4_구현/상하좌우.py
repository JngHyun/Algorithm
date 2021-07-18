import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-2.구현/input.txt')


N = int(input())
way = list(map(str,input().split()))
import time
start_time = time.time()

way_dict = {'R':[1,0],
        'L':[-1.0],
        'U':[0,-1],
        'D':[0,1]}


result = [1,1]

for w in way:
    result[0] += way_dict[w][0]
    result[1] += way_dict[w][1]
    if result[0] >5 or result[0] < 1 or result[1]>5 or result[1] < 1:
        result[0] -= way_dict[w][0]
        result[1] -= way_dict[w][1]
    
print(*result, end=' ')

end_time = time.time()
print("time" , end_time - start_time)

start_time = time.time()


dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types=['U','D','L','R']
x,y=1,1
nx = 0; ny =0
for w in way:
    for i in range(len(move_types)):
        if w == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
        if nx<1 or ny<1 or nx>N or ny>N:
            continue
        
        x,y = nx,ny
print(x,y)


end_time = time.time()
print("time" , end_time - start_time)