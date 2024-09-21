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
    for(let j = i+1;j<arr.length;++j){
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

// Optimal solution using stack - non-circular case
// Start from the end, pop all the elements from the stack that are lesser than the value at the current index. Once a larger element is found
// assign that value as nge of the current index and push the current element to the stack.
function nextGreaterElementUsingStack(arr){
  const stack = [];
  const res = [];

  for(let i = arr.length - 1; i>=0;--i){
    
    while(stack[stack.length - 1] !== undefined && stack[stack.length - 1] <= arr[i]){
      stack.pop();
    }

      
      if(stack[stack.length - 1] !== undefined){
        res[i] = stack[stack.length - 1];
      }else{
        res[i] = -1;
      }
       stack.push(arr[i])
    
  }
  return res;
  
}
