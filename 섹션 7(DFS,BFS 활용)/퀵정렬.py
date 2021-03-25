# 병합정렬 : 후위순위 정렬
# 퀵정렬 : 전위순위 정렬
# pivot 기준으로 큰값과 작은값이 모이도록 partition 수행
# 1) pos 맨 왼쪽, pivot 맨 오른쪽
# 2) for문 돌면서 중심점 보다 작으면 Pos 와 swap , pos 1 증가
# 3) for 문 다 돌면 rt와 pos swap
def Qsort(lt,rt):
    if lt<rt:
        '''
        partition
        '''
        pos = lt # 우리가 정렬하고자 하는 시작지점 (재귀호출 일어나기 때문에 0 하면 안됨)
        pivot = arr[rt] # 우리가 정렬하고자 하는 곳의 가장 오른쪽
        for i in range(lt,rt): # rt 전까지 for 문 돌면서
            if arr[i]<=pivot:
                arr[i] , arr[pos] = arr[pos] , arr[i] # 2)
                pos+=1
        arr[rt] , arr[pos] = arr[pos] , arr[rt] # 3)

        Qsort(lt,pos-1)
        Qsort(pos+1,rt)
        
                
if __name__=="__main__":
    arr = [45,21,23,36,15,67,11,60,20,33]
    print("Before sort: " ,end ="")
    print(arr)
    Qsort(0,9)
    print("After sort : ",end='')
    print(arr)