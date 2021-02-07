import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/4. 후위식 연산/in4.txt","rt")

a = input()
print(a)

stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        if x =='+':
            a = int(stack.pop())
            b = int(stack.pop())
            tmp = b+a
        elif x=='-':
            a = int(stack.pop())
            b = int(stack.pop())
            tmp = b-a 
        elif x=='*':
            a = int(stack.pop())
            b = int(stack.pop())
            tmp = b*a 
        elif x=='/':
            a = int(stack.pop())
            b = int(stack.pop())
            tmp = b/a
        stack.append(tmp)
            
print(tmp)

    
