import sys
sys.stdin = open("/Users/pjh/Desktop/박정현/python_algorithm/섹션 5/9. 아나그램(구글)/in4.txt","rt")

a = input()
b = input()

def anagram(n):
    check = dict()
    for x in n:
        if x not in check.keys():
            check[x] = 1
        else:
            check[x] = check[x]+1
        # check[x]=check[x].get(x,0) + 1
    return check
        
a = anagram(a)
b = anagram(b)

if a==b:
    print('YES')
else:
    print('NO')

# 다르게 비교하기
'''
for i in a.keys():
    if i in b.keys():
        if a[i] != b[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else: print()
'''

