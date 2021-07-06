import sys
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/이코테/Code/1. 그리디&구현/input.txt')

data = input()

result = int(data[0])

for s in data:
    num = int(s)
    if num<=1 or result <=1:
        result += num
    else:
        result *= num

print(result)

'''
S = input()
result = 0
for s in S:
    if s == '0' or s == '1' or result <=1 :
        result+=int(s)
    else:
        result*=int(s)
    
print(result)
'''





