// Bubble sort

/** 
In bubble sorting, adjacent elements are compared and swapped with each other until the complete array is sorted.
Time complexity: O(N^2)

If this loop is run on a sorted array, we can use a flag and break out of the loop if no elements were swapped, reducing the time complexity to O(N);
*/

function bubbleSort(arr){

  for(let i=n-1;i>=0;--i){
    let didSwap = false;
    for(let j=0;j<i-1;++j){
      
      if(arr[j]>arr[j+1]){
        let temp = arr[j];
        a[j] = a[j+1];
        a[j+1] = temp;
        didSwap = true;
      }
    }

    if(!didSwap){
      break;
    }
  }
}


// Selection sort

/** 
In selection sort, upon each iteration, the minimum valued item is switched with the first index of each iteration. The iteration goes from i=0 to i=n-1, so in first iteration, the minimum value
of array is swapped with the item at i=0, similarly in the second iteration, the second smallest value is swapped with item at i=1 and so forth.
*/



function selectionSort(arr){

  for(let i=0;i<n;++i){

    let min = Infinity;
    for(let j=i;j<n;++j){
      if(arr[j]<min){
        min = arr[j];
      }
    }
    let temp = arr[i];
    arr[i] = min;
    min = temp;
  }
}
