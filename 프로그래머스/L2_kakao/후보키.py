from itertools import combinations

def solution(relation):
    res = []
    answer = 0

    # relation row/col 길이
    if relation:
        col_num = len(relation[0])
        row_num = len(relation)

    # 모든 조합
    all = []
    for i in range(1,col_num+1):
        all += [set(group) for group in combinations(list(range(col_num)),i)]

    for comb in all:
        check = set()
        for r in relation:
            sum = ''
            for c in comb:
                sum = sum + r[c]
            check.add(sum)

        #유일성 검정
        if len(check) == row_num:
            res.append(comb)

    #최소성 검정
    min = []
    for c in res:
        white_flag=0
        if not min:
            min.append(c)
        else:
            for m in min:
                if m.issubset(c):
                    white_flag = 1

        if white_flag ==0:
            min.append(c)

    answer = len(min)-1

    return answer