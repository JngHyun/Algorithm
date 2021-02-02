import sys
from collections import deque
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/7. 교육과정 설계/in4.txt","rt")

order = input()
n = int(input())


for i in range(n):
    res = ''
    chars = deque(input())
    for _ in range(len(chars)):
        char = chars.popleft()
        if str(char) in order:
            if len(chars) == 0:
                res+=char
            else:
                if chars[0] !=char:
                    res+=char
        if res == order:
            print('#%d YES'%(i+1))
            break
    else:
        print('#%d NO'%(i+1))



        

        








    
    















