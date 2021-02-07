import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/3. 후위표기식 만들기/in1.txt","rt")

a = input()

stack_op = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x =='(':
            stack_op.append(x)
        elif x ==')':
            while stack_op and stack_op[-1] != '(':
                res += stack_op.pop()
            stack_op.pop()
        elif x == '*' or x =='/':
            while stack_op and (stack_op[-1] == '*' or stack_op[-1] =='/'):
                res += stack_op.pop()
            stack_op.append(x)
        elif x == '+' or x =='-':
            while stack_op and stack_op[-1] != '(':
                res += stack_op.pop()
            stack_op.append(x)
while stack_op:
    res+=stack_op.pop()
print(res)