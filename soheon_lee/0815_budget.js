function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => {
  if (a < b) {
    return -1;
  }
  if (a > b) {
    return 1;
  }
  return 0;
  });
  for (let i = 0; i < d.length; i++) {
    budget -= d[i]
    if (budget < 0) {
      return answer
    }
    answer++
  }
  return answer
}

solution([2, 12], 1)
solution([1, 2, 3, 1], 10)
