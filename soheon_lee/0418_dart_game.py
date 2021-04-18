import datetime

def solution(dartResult):
    scores = []
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for i, elem in enumerate(dartResult):
        if elem.isdigit():
            if i != 0 and dartResult[i-1].isdigit():
                scores[-1] *= 10
                scores[-1] += int(elem)
                continue

            scores.append(int(elem))

        if elem.isalpha():
            scores[-1] = scores[-1]**bonus[elem]
            continue

        if elem == '*':
            if len(scores) == 1:
                scores[0] *= 2
                continue

            else:
                scores[-1] *= 2
                scores[-2] *= 2
                continue

        if elem == '#':
            scores[-1] *= -1
            continue

    return sum(scores)
a = datetime.datetime.now()
print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
b = datetime.datetime.now()
print(b-a)
