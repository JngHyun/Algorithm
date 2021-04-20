def solution(dartResult):
    answer = 0
    temp = []
    flag = True
    for i in dartResult:
        if i in ['S','D','T','#','*']:
            flag = True
            if i =='S':
                temp.append(num)
            elif i == 'D':
                temp.append((num)**2)
            elif i == 'T':
                temp.append((num)**3)
                
            elif i == '#':
                num = temp.pop(-1)
                temp.append(num*(-1))
            elif i == '*':
                if len(temp) > 1:
                    num1 = temp.pop()
                    num2 = temp.pop()
                    temp.append(num2*2)
                    temp.append(num1*2)
                else:
                    num = temp.pop(-1)
                    temp.append(num*2)
        else:
            if flag == True:
                num = int(i)
            elif flag == False:
                pre_num = str(num)
                num = int(pre_num + i)

            flag = False
                 
    answer = sum(temp)

    return answer