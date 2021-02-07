import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/9. 아나그램(구글)/in4.txt","rt")

a = input()
b = input()

sH = dict()

for x in a:
    sH[x] = sH.get(x,0) + 1

for x in b:
    sH[x] = sH.get(x,0) - 1

for x in a:
    if sH.get(x) != 0:
        print("NO")
        break
else:
    print("YES")
    