let players = ["mumu", "soe", "poe", "kai", "mine"]
let callings = ["kai", "kai", "mine", "mine"]

function solution(players, callings) {
  const playersObj = {}
  for (let i = 0; i < players.length; i++) {
    playersObj[players[i]] = i
  }

  callings.forEach((name) => {
    const curIdx = playersObj[name]
    const forwardPlayer = players[curIdx - 1]

    playersObj[forwardPlayer] = curIdx
    playersObj[name] = curIdx - 1

    players[curIdx] = forwardPlayer
    players[curIdx - 1] = name
  })

  return players
}
console.log(solution(players, callings))
