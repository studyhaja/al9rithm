function solution(scores) {
    let answer = '';
    let grades = [];
    let grade = ''
    for(let i=0; i<scores.length; i++){
        let sum=0;
        let min=101; 
        let max=-1;
        let avg=0;
        let len = scores.length;
        for(let j=0; j<scores[i].length; j++){
            max = Math.max(max,scores[j][i])
            min = Math.min(min,scores[j][i])
            sum+=scores[j][i];
        }
        let maxCount = 0;
        let minCount = 0;
        
        console.log(max)
        console.log(min)
        for(let j=0; j<scores[i].length; j++){
            if(scores[j][i] == max){
                maxCount++;
            }else if(scores[j][i] == min){
                minCount++;
            }
        }
      
        if( (maxCount==1 && max == scores[i][i]) || (minCount == 1 && min == scores[i][i]) ){
            sum -= scores[i][i];
            avg = sum / (len-1);
        }else{
            avg = sum / len;
        }
        console.log(sum)
        
        if(avg>=90){
            grade = 'A'
        }else if(avg<90 && avg>=80){
            grade = 'B'
        }else if(avg<80 && avg>=70){
            grade = 'C'
        }else if(avg<70 && avg>=50){
            grade = 'D'
        }else{
            grade = 'F'
        }
        grades[i] = grade
        console.log(grades)
        answer +=grades[i]
    }
    return answer;
}
