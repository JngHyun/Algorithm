import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 8(동적계획법)/10. 동전교환/in5.txt')

if __name__ =="__main__":
    n = int(input())
    coin = list(map(int,input().split))
    m = int(input())
    dy = [1000] *(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i],m+1):
            dy[j] = min(dy[j],dy[j-coin[i]+1])
    
    print(dy[-1])