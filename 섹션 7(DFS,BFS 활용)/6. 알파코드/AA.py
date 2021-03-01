import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/6. 알파코드/in5.txt')

def DFS(x,p):
    global cnt
    if x==n:
        cnt +=1
        for j in range(p):
            print(chr(64+res[j]),end='') # 65 : 'A'
        print()
    else:
        for i in range(1,27):
            if code[x] == i:
                res[p]=i
                DFS(x+1,p+1)
            elif i>=10 and code[x]==i//10 and code[x+1]==i%10:
                res[p]=i
                DFS(x+2,p+1)

if __name__ == '__main__':
    code = list(map(int,input()))
    n = len(code)
    code.insert(n, -1) # 마지막 숫자 2자리 수 확인 시 오류나지 않도록 함
    # 숫자가 26까지 돌기 때문에
    # 마지막 숫자가 3이상이면 elif문 조건에 아예 맞지 않기 때문에, 오류가 나지 않지만
    # 2이하인 경우에는 없는 자리까지 확인해 list index out of range 오류가 난다.
    res = [0]*len(code)
    cnt = 0
    DFS(0,0)
    print(cnt)

    
    


