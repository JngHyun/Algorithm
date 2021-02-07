import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/2. 쇠막대기/in4.txt","rt")

bar = input()

stack = []
cnt = 0

for i in range(len(bar)):
    if bar[i] =='(':
        stack.append(bar[i])
    else:
        stack.pop() 
        if bar[i-1] == '(' :
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)

