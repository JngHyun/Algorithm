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
    '''
    if s.isalpha():
        chars+=s
        
    else:
        sum += int(s)
    '''

    
chars.sort()

#숫자가 없는 경우도 꼭 체크해주어야 함
if sum != 0:
    chars.append(str(sum))

print(''.join(chars))

