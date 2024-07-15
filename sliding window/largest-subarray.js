function largestSummation(arr){

  let largestSum = -Infinity;

  for(let i=0;i<arr.length;++i){
    let sum = 0;
    for(let j = i; j< arr.length;++j){

      sum += arr[j];

      largestSum = Math.max(largestSum, sum);
    }
  }

  return largestSum;
}

console.log(largestSummation([-2,5,-1,-7,10]))
