def solution(board, moves):
    basket = []
    answer = 0

    for move in moves:
        index = move - 1
        print("MOVE: ", move)
        for row in board:
            target = row[index]
            print(row)
            if target == 0:
                continue
            if basket == []:
                basket.append(target)
                row[index] = 0
                print('BASKET: ', basket)
                break
            if basket[-1] == target:
                answer += 2
                basket.pop()
                row[index] = 0
                print('BASKET: ', basket)
                break
            else:
                basket.append(target)
                row[index] = 0
                print('BASKET: ', basket)
                break
        print('-------------------')

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
