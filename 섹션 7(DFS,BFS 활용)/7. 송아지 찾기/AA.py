import sys
import time
sys.stdin = open('/Users/pjh/Desktop/박정현/python_algorithm/섹션 7(DFS,BFS 활용)/7. 송아지 찾기/in5.txt')
st = time.time()
s,e = map(int,input().split())
if e<s:
    print(s-e)
elif e>=s:
    k = e-s
    if k < 5:
        print(k)
    elif k>=5:
        ch1 = k//5*5-k
        ch2 = (k//5+1)*5-k
        step = min(abs(ch1),abs(ch2))
        if abs(ch1)<abs(ch2):
            print(k//5+step)
        else:
            print(k//5+1+step)
et = time.time()
print(et-st)