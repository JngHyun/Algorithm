import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/3. 양팔저울/in5.txt')

def DFS(x,sum):
    if x>=k:
        res.append(abs(sum))
    else:
        DFS(x+1, sum + chu[x])
        DFS(x+1, sum - chu[x])
        DFS(x+1, sum)

if __name__ == '__main__':
    k = int(input())
    chu = list(map(int,input().split()))
    s = sum(chu)
    sum = 0
    ch = [0] * k
    res = list()
    DFS(0,sum)
    print(s-len(set(res))+1)
