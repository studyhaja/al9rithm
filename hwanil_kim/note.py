def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for b in board:
            if b[i-1] != 0:
                moved_num = b[i-1]
                b[i-1] = 0
                if len(stack) == 0:
                    stack.append(moved_num)
                else:
                    if stack[-1] == moved_num:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(moved_num)
                break
    return answer