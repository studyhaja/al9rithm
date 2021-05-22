const prefixAverageSummationOn1 = (originalArr) => {
  const prefixAvg = []
  for (i = 0; i < originalArr.length; i++) {
    const partialSum = originalArr.slice(0, i+1).reduce(function(a, b) { return a + b; }, 0);
    prefixAvg.push(partialSum/(i+1))
  }

  return prefixAvg
}

console.log(prefixAverageSummationOn1([1, 2, 3]))

const prefixAverageSummationOn2 = (originalArr) => {
  const prefixAvg = [];
  let sum = 0;
  for (i = 0; i < originalArr.length; i++) {
    sum += originalArr[i]
    prefixAvg.push(sum/(i + 1))
  }
  return prefixAvg
}

console.log(prefixAverageSummationOn2([1, 2, 3]))
