
from collections import deque


def solution(dice):
    i = 0
    while i < 9999:
        number = i
        Ndice = dice[:]
        i = deque(list(str(i)))
        while i:
            now = int(i.popleft())
            for idx, case in enumerate(Ndice):
                if now in case:
                    del Ndice[idx]
                    break
            else:
                print(number)
                return number
        i = number + 1
    print(-1)
    return -1


# solution([[1, 2, 3, 4, 6, 7, 5], [0, 6, 4, 3, 6, 0, 9], [1, 2, 0, 5, 6, 7, 8]])
solution([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
