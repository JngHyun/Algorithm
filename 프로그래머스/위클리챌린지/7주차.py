from itertools import combinations

def solution(enter, leave):
    answer = [0] * len(enter) #정답
    before = [] # 전에 들어온 사람 저장
    before_compare = [] # 중복 제거를 위한 비교 리스트

    for l in leave:

        if l not in before: #before에 포함되어 있는 경우 이미 체크되어 있기 때문에 제외

            before = enter[:enter.index(l)+1] # 전에 들어온 사람 모두 저장

            if len(before) > 1:
                same = list(set(before) & set(before_compare)) #이전과 같은 사람들이 중복으로 카운팅 되지 않도록 중복 사람 체크

                if len(same)<2: #중복되는 사람이 없다면 각각 추가
                    for s in before:
                        answer[s-1] += len(before)-1
                else: #중복되는 사람이 있다면
                    for s in before: 
                        if s in same: #중복인 사람한테는 중복 제거 한 인원 추가
                            answer[s-1] += len(before)-len(same)
                        else: # 새로운 사람한테는 모두 추가
                            answer[s-1] += len(before)-1

        before_compare = before    
        enter.remove(l)    

    return answer
