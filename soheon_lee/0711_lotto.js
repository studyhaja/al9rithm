function solution(lottos, win_nums) {
    var answer = [0,0];

    const zero = lottos.filter(v=>!v).length
    const haslottos = lottos.filter((el,index)=> win_nums.includes(el)).length
    const maxlottos = haslottos +zero
    if (haslottos>1){
       answer = [7-maxlottos,7-haslottos]
    } else{
        if(maxlottos>0 ){
            answer = [7-maxlottos,6]    
        } else{
            answer = [6,6]
        }

    }

    return answer;
}
