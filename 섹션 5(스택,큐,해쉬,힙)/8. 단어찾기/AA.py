import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/8. 단어찾기/in2.txt","rt")

n = int(input())
letters = []
for i in range(n):
    letters.append(input())

for i in range(n-1):
    a = input()
    if a in letters:
        letters.remove(a)

print(letters[0])
