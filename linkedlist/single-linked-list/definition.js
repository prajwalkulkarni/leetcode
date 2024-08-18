const arr = [1,2,3,4,5,6,7,8]



class Node{

  constructor(data, next=null){
    this.data = data;
    this.next = next;
  }
}
function arrayToLinkedList(arr){
  const headData = arr[0];
  const head = new Node(headData);
  let mover = head;

  for(let i = 1; i<arr.length;++i){
    const temp = new Node(arr[i]);
    mover.next = temp;
    mover = temp;
  }

  return head;
}
