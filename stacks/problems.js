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

// Optimal solution - circular array, duplicate the array, and push it to the original array so that all the elements behind an element also come next to it.
function nextGreaterElementUsingStack(arr){
  const stack = [];
  const res = [];

  for(let i = 2 * arr.length - 1; i>=0;--i){
    
    while(stack[stack.length - 1] !== undefined && stack[stack.length - 1] <= arr[i % arr.length]){
      stack.pop();
    }

      
      if(stack[stack.length - 1] !== undefined){
        res[i] = stack[stack.length - 1];
      }else{
        res[i] = -1;
      }
       stack.push(arr[i % arr.length])
    
  }
  return res.slice(0, arr.length);
  
}


/*

Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Input Format

The only argument given is integer array A.
Output Format

Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be -1.
For Example

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
*/

function nextSmallerElement(arr){
   const stack = [];
  const res = [];

  for(let i = 0; i<arr.length;--i){
    
    while(stack[stack.length - 1] !== undefined && stack[stack.length - 1] >= arr[i]){
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

