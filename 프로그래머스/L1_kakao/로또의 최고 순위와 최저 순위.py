order={6:1,5:2,4:3,3:4,2:5,1:6,0:6} # order = [6,6,5,4,3,2,1] 로 대체 후 index를 순위로 반환 가능
def solution(lottos, win_nums):
    answer = [];
    blind = 0; score =0
    for i in lottos:
        if i ==0: 
            blind +=1 # lottos.count(0) 으로 대체 가능
        elif i in win_nums: 
            score+=1
            
    max = order[score+blind]
    min = order[score]
            
    answer = [max,min]
    return answer

    # 1과 0에 대한 점수를 dictionary로 넣어주는 방법으로 코드를 더 짧게 만들 수 있다.
    
