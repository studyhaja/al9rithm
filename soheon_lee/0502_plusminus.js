function solution(absolutes, signs) {
  let answer = 0;
  
  for (let i = 0; i < absolutes.length; i++) {
    answer = answer + absolutes[i] * (signs[i] ? 1 : -1)
  }
  return answer;
}

console.log(solution([4, 7, 12], [true, false, true]))
