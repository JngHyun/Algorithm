from collections import Counter
import string
def solution(str1, str2):
    answer = 0; union = 0; all = 0; outer = 0

    alp = string.ascii_lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    str1_s = [str1[i:i+2] for i in range(len(str1)) if len(str1[i:i+2])==2]
    str2_s = [str2[i:i+2] for i in range(len(str2)) if len(str2[i:i+2])==2]

    str1_s = [i for i in str1_s if (i[0] in alp and i[1] in alp)]
    str2_s = [i for i in str2_s if (i[0] in alp and i[1] in alp)]

    str1_c = Counter(str1_s)
    str2_c = Counter(str2_s)

    same = str1_c.keys()&str2_c.keys()

    for i in str1_c:
        if i not in same:
            outer += str1_c[i]
    for j in str2_c:
        if j not in same:
            outer += str2_c[j]

    if len(same)>0:
        for s in same:
            all += max(str1_c[s], str2_c[s])
            union += min(str1_c[s], str2_c[s])

        answer = int((union/(outer+all))*65536)
    else:
        if outer ==0:
            answer = 65536
        else:
            answer =0     
    return answer

