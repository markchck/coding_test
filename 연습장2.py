def solution(dice):
    length = len(dice)
    items = []

    for i, case in enumerate(dice):
        A = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        B = set(case)
        items.append((A-B))

    temps = [0] * 10
    for item in items:
        for i in item:
            temps[i] += 1

    result = []
    for i in range(1, len(temps)):
        if temps[i] >= (length / 2):
            count = 0
            for case in dice:
                if i not in case:
                    count += 1

            if length % 2 == 0:
                result.append(str(i) * (count + 1))
            else:
                result.append(str(i) * (count))
            break
    print(temps)
    for re in result:
        print(re)
        return int(re)


solution([[1, 2, 4, 5, 6, 8], [0, 3, 9, 5, 6], [1, 6, 8, 9, 3]])
