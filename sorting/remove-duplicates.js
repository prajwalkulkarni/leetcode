// Two pointer solution for removing duplicate elements from a sorted array


function removeDuplicates(arr){

  let i = 0;

  for(let j=1;j<arr.length;++j){
    if(arr[j]!==arr[i]){
      ++i;
      arr[i] = arr[j]
    }
  }

  for(let k = 0;k<i+1;++k){
    console.log(arr[k])
  }
}
