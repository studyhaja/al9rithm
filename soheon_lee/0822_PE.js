function solution(n, lost, reserve) {
  var answer = n - lost.length;

  lost.sort((a, b) => a-b)
  reserve.sort((a, b) => a-b)

  const newLost = []

  for (let i = 0; i < lost.length; i++) {
    const target = lost[i]
    if (reserve.includes(target)) {
      answer ++;
      reserve.splice(reserve.indexOf(target), 1);
      continue;
    }
    newLost.push(target)
  }

  for (let i = 0; i < newLost.length; i++) {
    if (reserve.includes(newLost[i] - 1) || reserve.includes(newLost[i] + 1)) {
      const target = reserve.includes(newLost[i] - 1) ? newLost[i] - 1 : newLost[i] + 1;
      answer++;
      reserve.splice(reserve.indexOf(target), 1);
      continue;
    }
  }

  return answer;

  // lost랑 reserve를 둘 다 오름 차순 정렬.
  // 우선, lost의 for loop 돌면서,
  // 
  // 나보다 1 작거나 큰 숫자가 있다?
  // yes -> answer++;
  // 그럼 이제 3은 해 reserve에서 사라져야지.
  // no -> 다음 루프.

}

console.log(solution(5, [2, 4], [1, 3, 5]))
console.log(solution(5, [2, 4], [3]))
console.log(solution(3, [3], [1]))
console.log(solution(5, [2, 3, 4], [3, 4, 5]))
