var sumOfUnique = function(nums) {
  const uniqueNums = {};
  let answer = 0;
  for(let i=0; i<nums.length; i++){
    if(uniqueNums[nums[i]]===0) continue
    if(uniqueNums[nums[i]]){
      uniqueNums[nums[i]]=0;
    } else{
      uniqueNums[nums[i]] = nums[i];
    }
  }
  for(const num in uniqueNums) answer+=uniqueNums[num];
  return answer;
};
