def solution(sizes):
    answer = 0
    for idx, s in enumerate(sizes):
        if s[1] > s[0]:
            sizes[idx][0],sizes[idx][1] = sizes[idx][1],sizes[idx][0]

    answer = max([s[0] for s in sizes]) * max([s[1] for s in sizes]) 
    return answer