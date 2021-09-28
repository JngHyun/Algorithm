import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        answer +=1
        
        if len(scoville)==1:
            if scoville[0] < K:
                answer = -1
                break
        
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville,s1+(s2*2))


        
         
    return answer