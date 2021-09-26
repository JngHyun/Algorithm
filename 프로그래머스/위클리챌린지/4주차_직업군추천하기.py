def solution(table, languages, preference):
    table = [t.split(' ') for t in table]
    scores = [[6-t.index(l) if l in t else 0 for l in languages] for t in table]
    print(scores)
    total_score = [sum(map(lambda x,y:x*y,score,preference)) for score in scores]
    mtc = max(total_score)
    answer = [table[i][0] for i,ts in enumerate(total_score) if ts==mtc] 
    answer.sort()
    answer = answer[0]

    return answer
