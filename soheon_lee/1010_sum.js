
function solution(numbers) {

  const reducer = (accumulator, curr) => accumulator + curr;
  const sum = numbers.reduce(reducer)

  return 45 - sum
}

