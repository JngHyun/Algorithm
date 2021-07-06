import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1-2.구현/input.txt')

String = input()
num = [str(i+1) for i in range(9)]

sum = 0
chars = []
for s in String:
    if s in num:
        sum += int(s)
    else:
        chars+=s
    
chars.sort()
if sum != 0:
    chars.append(str(sum))

print(''.join(chars))

