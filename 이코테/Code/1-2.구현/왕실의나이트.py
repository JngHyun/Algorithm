import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-2.구현/input.txt')

a = input()
col=a[0]
row_idx=int(a[1])
alphabet= [0,'a','b','c','d','e','f','g','h']
col_idx = int(alphabet.index(col))



dx = [-2,2,-2,2,-1,1,-1,1]
dy = [-1,-1,1,1,-2,-2,2,2]

count = 0 
for i in range(len(dx)):
    cy = col_idx + dx[i]
    cx = row_idx + dy[i]

    if cx<=8 and cx>=1 and cy<=8 and cy>=1:
        count+=1

print(count)




