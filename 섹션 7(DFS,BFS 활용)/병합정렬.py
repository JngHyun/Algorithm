# 병합정렬
# 1. lt부터 rt까지의 영역을 두개로 나눔
# 2. 나눠진 왼쪽과 오른쪽을 각각 호출한다. (lt<rt까지)
# 3. 그 밑에서 본연의 일(두 리스트 합치기)을 코드로 짠다.

def Dsort(lt,rt):
    if lt<rt:
        # 1. 
        mid = (lt+rt)//2
        
        # 2.
        Dsort(lt,mid)
        Dsort(mid+1,rt)

        #3, 정렬된 리스트 합치는 것
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid:
            tmp += arr[p1:mid+1]
        if p2<rt:
            tmp+=arr[p2:rt+1]
        # 합쳐진 리스트 원래 arr에 복사하기
        for i in range(len(tmp)):
            arr[lt+i]=tmp[i]
            
if __name__=='__main__':
    arr = [23,11,45,36,15,67,33,21]
    print("Before sort : ", end='')
    print(arr)
    Dsort(0,7)
    print("After sort : ",end ='')
    print(arr)
