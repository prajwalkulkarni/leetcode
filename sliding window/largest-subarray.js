// Brute force

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

console.log(largestSummation([-2,5,-1,-7,10,5,2,-1,4,-3,-2]))


// Better

function largestSummation(arr){

  let largestSum = -Infinity;

  let l,r;
  l = r = 0;
  let sum = 0;
  while(r < arr.length){
    sum+= arr[r];
    while(arr[r]>sum){
      sum -= arr[l]
      l+=1;
    }
    largestSum = Math.max(sum, largestSum);
    r+=1;
  }

  return largestSum

  
}
