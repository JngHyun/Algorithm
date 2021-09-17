import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/Chap4_구현/input.txt')

data = input()
char = []
sum=0
for x in data:
    if x.isalpha():
        char.append(x)
    else:
        sum+=int(x)

char = sorted(char)
answer = ''.join(char) + str(sum)

if sum == 0:
    answer = ''.join(char)
print(answer)

