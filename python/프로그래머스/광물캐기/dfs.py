table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
res = 9876756543
m = dict()
m['diamond'] = 0
m['iron'] = 1
m['stone'] = 2


def dfs(idx, d, ir, s, minerals, price):  # 상승식이든 하강식이든 idx가 필요함
    # 종료조건 (도구가 없거나, 광물이 없거나)
    if (d == 0 and ir == 0 and s == 0 or idx >= len(minerals)):
        global res
        # 종료조건은 res 업데이트할 기회
        res = min(res, price)
        return

    # 가격을 구하는게 목표임
    diaPrice = 0
    iroPrice = 0
    stoPrice = 0
    for i in range(idx, min((idx+5), len(minerals))):
        # i번째 미네랄을 dia로 채취할 때 들어가는 비용의 누적
        diaPrice += table[0][m[minerals[i]]]
        iroPrice += table[1][m[minerals[i]]]
        stoPrice += table[2][m[minerals[i]]]
    if d > 0:
        d -= 1
        dfs(idx+5, d, ir, s, minerals, price + diaPrice)
    if ir > 0:
        ir -= 1
        dfs(idx+5, d, ir, s, minerals, price + iroPrice)
    if s > 0:
        s -= 1
        dfs(idx+5, d, ir, s, minerals, price + stoPrice)


def solution(picks, minerals):
    global res
    dfs(0, picks[0], picks[1], picks[2], minerals, 0)
    return res


solution([1, 3, 2], ["diamond", "diamond", "diamond",
         "iron", "iron", "diamond", "iron", "stone"])
