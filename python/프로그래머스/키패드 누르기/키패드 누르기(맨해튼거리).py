def solution(numbers, hand):
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2), "*": (3, 0), 0: (3, 1), "#": (3, 2)}

    nowL = pad["*"]
    nowR = pad["#"]

    pressL = [1, 4, 7, "*"]
    pressR = [3, 6, 9, "#"]
    press = [2, 5, 8, 0]

    answer = ''

    for num in numbers:
        now = pad[num]
        if num in pressL:
            answer += 'L'
            nowL = now
        # 3,6,9인 경우
        elif num in pressR:
            answer += 'R'
            nowR = now
        # 2,5,8,0인 경우
        else:
            countR = abs(nowR[0] - now[0]) + abs(nowR[1] - now[1])
            countL = abs(nowL[0] - now[0]) + abs(nowL[1] - now[1])
            if countR > countL:
                answer += 'L'
                nowL = now
            elif countR < countL:
                answer += 'R'
                nowR = now
            else:
                if hand == "right":
                    answer += 'R'
                    nowR = now
                else:
                    answer += 'L'
                    nowL = now
    print(answer)
    return (answer)


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
