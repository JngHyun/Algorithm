from itertools import combinations

def solution(info, query):
    answer = []
    db = {}
    for i in info:
        temp = i.split()
        contents = temp[:-1]
        value = int(temp[-1])

        for j in range(5):
            comb = list(combinations(range(4),j))
            for c in comb:
                conditions = contents.copy()
                for idx in c:
                    conditions[idx] = '-'
                condition = ''.join(conditions)
                if condition in db:
                    db[condition].append(value)
                else:
                    db[condition] = [value]

    for value in db.values():
        value.sort()

    for q in query:
        q = [i for i in q.split() if i !='and']
        q_condition = ''.join(q[:-1])
        q_value = int(q[-1])
        if q_condition in db:
            data = db[q_condition]
            if len(data)>0:
                start,end = 0, len(data)
                while start != end and start != len(data):
                    mid = (start+end)//2
                    if data[mid]>=q_value:
                        end = mid
                    else:
                        start = (start+end)//2+1
                answer.append(len(data)-start)
        else:
            answer.append(0)

    return answer