import sys
from collections import Counter 
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/9. 아나그램(구글)/in4.txt","rt")


a = [x for x in input()]
b = [y for y in input()]

a = Counter(a)
b = Counter(b)

if a==b:
    print('YES')
else:
    print('NO')
