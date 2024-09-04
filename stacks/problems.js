// Next greater element
/**
Problem Statement: Given a circular integer array A, return the next greater element for every element in A. The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. If it doesn't exist, return -1 for this element.

Examples:

Example 1: 

Input: N = 11, A[] = {3,10,4,2,1,2,6,1,7,2,9}

Output: 10,-1,6,6,2,6,7,7,9,9,10

*/


//Brute force
function nextGreaterElement(arr){

  const sol = [];
  for(let i = 0;i<arr.length;++i){
    for(let j = i;i<arr.length;++j){
      if(arr[j]>arr[i]){
        sol[i] = arr[j];
        break;
      }
    }
    if(typeof sol[i] !== 'number'){
      for(let k=0;k<i;++k){
        if(arr[k]> arr[i]){
          sol[i] = arr[k];
          break;
        }
      }
    }
    if(typeof sol[i] !== 'number'){
      sol[i] = -1;
    }
  }
  return sol
}
