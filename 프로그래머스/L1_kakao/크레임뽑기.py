def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] =0
                break
        if len(basket)>1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer