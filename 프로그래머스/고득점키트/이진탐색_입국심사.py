def solution(n, times):
    # 가장 시간이 오래걸리는 경우
    rt = max(times) * n
    lt = 1
    answer = 0

    while lt<=rt:
        # mid 값 계산
        mid = (rt+lt)//2
        total = 0

        # mid가 몇명을 심사할 수 있는지 확인하기
        for time in times:
            total += mid//time
            if total >= n: break;

        # mid가 n명 이상 심사할 수 있는 경우
        if total>=n:
            answer = mid
            rt = mid -1
        # mid가 n명 이하만 심사할 수 있는 경우
        else:
            lt = mid + 1

    return answer