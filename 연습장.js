import sys
table=  {
    "dia":{
        "diamond" : 1,
        "iron" :1,
        "stone" : 1
    },
    "iron":{
        "diamond":5,
        "iron":1,
        "stone":1
    },
    "stone":{
        "diamond":25,
        "iron":5,
        "stone":1
    }
}
answer = 0
def calculate(tool,minerals, tiredness):
    for(i=0; i < min(len(minerals), 5), i++){
        if(tool=="dia"):
            tiredness += table[tool[minerals[i]]]
        if(tool=="iron"):
            tiredness += table[tool[minerals[i]]]
        if(tool=="stone"):
            tiredness += table[tool[minerals[i]]]
    }
    if(len(minerals) < 5):
        minerals = []
    else:
        minerals= minerals[5:]
    return (minerals, tiredness)
    
    
        
def recursion(d,i,s, minerals, tiredness ):
    global answer
    left=len(minerals)
    if(sum(d,i,s) == 0 or left == 0):
        answer = min(answer, tiredness)
        return
    else:
        if(d>0):
            newMinerals, newTiredness= calculate("dia", minerals, tiredness)
            recursion(d-1, i, s, newMinerals, newTiredness )
        if(i>0):
            newMinerals, newTiredness= calculate("iron", minerals, tiredness)
            recursion(d, i-1, s, newMinerals, newTiredness )
        if(s>0):
            newMinerals, newTiredness= calculate("stone", minerals, tiredness)
            recursion(d, i, s-1, newMinerals, newTiredness )
    
        
def solution(picks, minerals):
    d,i,s=picks
    recursion(d,i,s, minerals, 0)
    return answer