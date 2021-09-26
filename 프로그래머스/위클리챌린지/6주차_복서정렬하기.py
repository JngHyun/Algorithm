def solution(weights, head2head):
    win_rate = []
    heavy_count = []
    nums = []
    for idx,h in enumerate(head2head):
        round = [x for x in h if x=='W' or x=='L']
        if len(round)==0:
            win_rate.append(0)
        else:
            win_rate.append(round.count('W')/(len(round)))
        
        heavy_count.append(len([w for i,w in enumerate(weights) if w > weights[idx] and h[i]=='W'] ))
        nums.append(idx+1)

    res = [(wr,hc,w,n) for wr,hc,w,n in zip(win_rate,heavy_count,weights,nums)]
    res = sorted(res,key = lambda x:(x[0],x[1],x[2]),reverse=True)
    res = [r[-1] for r in res]

    return res

