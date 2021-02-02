import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/8. 단어찾기/in2.txt","rt")

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key,val in p.items():
    if val == 1:
        print(key)
        break