import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/5. 동전분배하기/in5.txt')

def DFS(x):
    global res
    if x == n:
        if len(set(total)) == 3:
            diff_min = max(total) - min(total)
            if diff_min <= res:
                res = diff_min
    else:
        for i in range(3):
            total[i] = total[i] + a[x]
            DFS(x+1)
            total[i] = total[i] - a[x]



if __name__=='__main__':
    n = int(input())
    a = list()
    total = [0]*3
    for i in range(n):
        a.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)
    
    