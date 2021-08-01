const forleft= [1,4,7] , forright=[3,6,9]
const move =(pos,num,curpos,hand)=>{
            console.log({curpos,num })

    if(forleft.includes(num)){
        // 왼손전용이동 
        curpos.left[0] = pos[num][0]; 
        curpos.left[1] = pos[num][1];    
        // console.log(curpos.left);
        return 'L'
    }
    else if(forright.includes(num)){
        // 오른손 전용이동 
        curpos.right[0] = pos[num][0]; 
        curpos.right[1] = pos[num][1];    
        return 'R'; 
    }
    else{
        // 양손이동  
        // console.log({pos,curpos,num})
        let distl = calculate(pos,curpos.left,num); 
        let distr = calculate(pos,curpos.right,num); 
        // console.log({curpos,num, distl,distr})
        if(distl===distr){
            if(hand==='left'){ 
                curpos.left[0] = pos[num][0]; 
                curpos.left[1] = pos[num][1];  
                return 'L';
            }
            else{ 
                curpos.right[0] = pos[num][0]; 
                curpos.right[1] = pos[num][1];    
                return 'R'; 
            } 
        }
        else if(distl < distr){
        curpos.left[0] = pos[num][0]; 
        curpos.left[1] = pos[num][1];  
            return 'L';
        }
        else{
        curpos.right[0] = pos[num][0]; 
        curpos.right[1] = pos[num][1];    
            return 'R'; 
        }  
    }
}

const calculate = (pos,curpos , num )=>{
    let x = curpos[0] - pos[num][0];
    let y = curpos[1]- pos[num][1];
    x = x<0 ? x*-1 : x; 
    y = y<0 ? y*-1 : y;   
    return x+y <0 ? (x+y)*(-1) : x+y; 
} 


function solution(n, hand) {
    let pos = {
         0 : [3,1] , 
         1 : [0,0] , 
         2 : [0,1] , 
         3 : [0,2] , 
         4 : [1,0] , 
         5 : [1,1] , 
         6 : [1,2] , 
         7 : [2,0] , 
         8 : [2,1] , 
         9 : [2,2] , 
    }; 
    let cur_pos = {
        left : [3,0],
        right: [3,2]
    }; 
    let answer = '';  
    for(let i =0 ; i<n.length ;i++){
        answer += move(pos,n[i],cur_pos,hand); 
    }
    return answer; 

}

