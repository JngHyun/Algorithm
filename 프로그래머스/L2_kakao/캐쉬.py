# 캐쉬 사이즈가 0인 조건 생각하기
# 캐쉬가 참조되는 경우 최근 참조 위치로 옮겨주는 과정 필요!
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize != 0:
        for city in cities:
            city = city.lower()
            if city not in cache:
                if len(cache)<cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            else: 
                cache.pop(cache.index(city))
                cache.append(city)
                answer +=1
    else: 
        answer += len(cities)*5
        
    return answer