def solution(numbers, hand):
    answer = ''
    points = {0:(0,0),
              '*':(-1,0),
              '#':(1,0),
              7:(-1,1),8:(0,1),9:(1,1),
              4:(-1,2),5:(0,2),6:(1,2),
              1:(-1,3),2:(0,3),3:(1,3)}
    
    left = '*'
    right = '#'
    
    for num in numbers:
        if num in [1,4,7]:
            left = num
            answer += 'L'
            
        elif num in [3,6,9]:
            right = num
            answer += 'R'
            
        else:
            left_dis = abs(points[num][0] - points[left][0]) + abs(points[num][1] - points[left][1])
            right_dis = abs(points[num][0] - points[right][0]) + abs(points[num][1] - points[right][1])
            if left_dis<right_dis:
                left = num
                answer +='L'
            elif left_dis>right_dis:
                right = num
                answer +='R'
            else:
                if hand == 'left':
                    left = num
                    answer +='L'
                else:
                    right = num
                    answer +='R'
    return answer