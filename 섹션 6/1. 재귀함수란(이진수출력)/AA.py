import sys
sys.stdin= open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 6/1. 재귀함수란(이진수출력)/in5.txt','r')

def binary(x):
    if x>=1:
        binary(x//2)
        print(x%2,end='')

if __name__ == "__main__":
    n = int(input())
    binary(n)

