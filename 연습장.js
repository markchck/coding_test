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
res = 98765434232

def dfs(idx, d, ir, s, minerals, price):
if(d ==0 and ir ==0 and s==0 or idx>=len(minerals)):
    global res
    res = min(res, price)
    return
else:
    diaPrice = 0
    iroPrice = 0
    stoPrice = 0
    for i in range(idx, min((idx+5), len(minerals))):
        diaPrice += table["dia"][minerals[i]]
        iroPrice += table["iron"][minerals[i]]
        stoPrice += table["stone"][minerals[i]]
    if d:
        dfs(idx+5, d-1, ir, s, minerals, price+diaPrice)
    if ir:
        dfs(idx+5, d, ir-1, s, minerals, price + iroPrice)
    if s:
        dfs(idx+5, d, ir, s-1, minerals, price + stoPrice)
        

def solution(picks, minerals):
global res
dfs(0,picks[0], picks[1], picks[2], minerals, 0)
return res


    
