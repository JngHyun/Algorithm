import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/11. 최대점수 구하기(냅색알고리즘)/in2.txt')

if __name__ == "__main__":
    n,m = map(int,input().split())
    dy = [0] *(m+1)
    for i in range(n):
        ps, pt = map(int,input().split())
        for j in range(m,pt-1,-1):
            dy[j] = max(dy[j], dy[j-pt]+ps)
        
    print(dy[m])