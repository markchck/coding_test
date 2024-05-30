
table = {
    "dia": {
        "diamond": 1,
        "iron": 1,
        "stone": 1
    },
    "iron": {
        "diamond": 5,
        "iron": 1,
        "stone": 1
    },
    "stone": {
        "diamond": 25,
        "iron": 5,
        "stone": 1
    }

}


def mining(tool, diaNum, ironNum, stoneNum, leftMinerals, result):

    count = 0
    while (count < 5 and len(leftMinerals) > 0):
        count += 1
        item = leftMinerals.pop(0)
        result += table.tool.item
    return result


def solution(picks, minerals):
    global table

    result = 0
    while (True):
        if (sum(picks) == 0 or not minerals):
            return result
        else:
            diaNum, ironNum, stoneNum = picks
            # 순서가 무작위인 점을 고려해야해! (백트레킹 필요하다)

            if (diaNum > 0):
                mining("dia", diaNum - 1, ironNum, stoneNum, minerals, result)
            if (ironNum > 0):
                mining("iron", diaNum, ironNum-1, stoneNum, minerals, result)
            if (stoneNum > 0):
                mining("stone", diaNum, ironNum, stoneNum-1, minerals, result)
