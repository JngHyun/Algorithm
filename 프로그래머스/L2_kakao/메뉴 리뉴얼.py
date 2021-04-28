from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        temp = {}
        for order in orders:
            com_order = list(combinations(list(order),c))
            for o in com_order:
                if set(o).issubset(order):
                    o = ''.join(sorted(o))
                    try: temp[o] += 1
                    except: temp[o] = 1
        if len(temp)>0:
            max_val = max(list(temp.values()))
            if max_val > 1:
                answer+=[key for key,val in temp.items() if val == max_val]
    answer = sorted(answer)
    return answer