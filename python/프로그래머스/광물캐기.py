def solution(picks, minerals):
    minerals = [list(minerals[i:i+5])
                for i in range(0, min(sum(picks)*5, len(minerals)), 5)]
    # [['diamond', 'diamond', 'diamond', 'iron', 'iron'], ['diamond', 'iron', 'stone']]
    req = []

    for bundle in minerals:
        tmp = [0, 0, 0]  # 다이아, 철, 돌 사용시 피로도
        for material in bundle:
            if (material == 'diamond'):
                tmp[0] += 1
                tmp[1] += 5
                tmp[2] += 25
            elif (material == 'iron'):
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 5
            else:
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 1
        req.append(tmp)  # [[5, 17, 85], [3, 7, 31]]
    req.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)

    ans = 0
    for score in req:
        if picks[0] > 0:
            ans += score[0]
            picks[0] -= 1
            continue
        if picks[1] > 0:
            ans += score[1]
            picks[1] -= 1
            continue
        if picks[2] > 0:
            ans += score[2]
            picks[2] -= 1
    return ans


solution([1, 3, 2], ["diamond", "diamond", "diamond", "diamond",
         "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])
