function solution(scores) {
    let length = scores.length
    let result = ''
    
    function transpose(a) {
        return Object.keys(a[0]).map(function(c) {
            return a.map(function(r) { return r[c]; });
        });
    }
    
    let transposed = transpose(scores)
    
    
    function sum (arr) {
        let r = 0
        for (let i = 0; i < arr.length; i++) {
            r += arr[i]
        }
        return r
    }

    const getGrade = score => {
        score = Number(score)
        if (90 <= score) {
            return 'A'
        } else if (80 <= score < 90) {
            return 'B'
        } else if (70 <= score < 80) {
            return 'C'
        } else if (50 <= score < 70) {
            return 'D'
        } else if ( score < 50) {
            return 'F'
        }
    }

    for (let i = 0; i < length; i++) {
        let self = scores[i][i]
        let numberOfSelf = transposed[i].filter(x => x == self).length
        let min = Math.min(...transposed[i])
        let max = Math.max(...transposed[i])

        console.log('self: ', self)
        console.log('numOfSelf: ', numberOfSelf)
      console.log('min: ', min)
      console.log('max: ', max)
        
        if (numberOfSelf == 1 && (self == min || self == max)) {
          console.log('self: ', self, ' and only')


            let avg = (sum(transposed[i]) - self) / (length - 1)
          console.log('avg!!!: ', avg)

          console.log('grade: ', getGrade(avg))
            result += getGrade(avg)
            
        }
        else if (!self == min || !self == max) {
            let avg = sum(transposed[i]) / length
            result += getGrade(avg)
            
        }
    }
    return result
}

console.log(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
