const findJudge = function(n, trust) {
  let numGot = {}
  let judge = []
  let from = []
  
  
  for (let i = 0; i < trust.length; i++) {
    from.push(trust[i][0])
    let target = trust[i][1]
    if (target in numGot) {
      numGot[target]++;
    } else {
      numGot[target] = 1;
    }
    
    if (judge.includes(trust[i][0])) {
      judge.splice(judge.indexOf(trust[i][0]), 1)
      judge.push(trust[i][1])
    } else {
      if (!judge.includes(trust[i][1])) {
        judge.push(trust[i][1])
      }
    }
  }
  if (judge.length === 0) {
      if (n===1) {
          return 1
      } else {
         return -1 
      }
    
  }
  let mightBeJudge = judge[0]
  
  if (numGot[mightBeJudge] < n-1) {
    return -1
  }

  if (from.includes(judge[0])) {
    return -1
  }
  return judge[0]
}
