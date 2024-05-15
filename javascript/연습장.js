function solution(x, y, n) {
  var answer = [[x, 0]]

  while (answer.length > 0) {
    const [value, count] = answer.shift()
    if (value === y) {
      return count
    }
    if (value < y) {
      answer.push(
        [2 * value, count + 1],
        [3 * value, count + 1],
        [value + n, count + 1]
      )
    }
  }
  return -1
}

console.log(solution(2, 5, 4))
