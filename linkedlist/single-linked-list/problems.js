// Find the middle element in linked list;


class Node{

  constructor(val, next = null){
    this.val = val;
    this.next = next;
}

function createDLL(){

  let arr = [1,2,3,4,5];

  const head = new Node(arr[0]);
  let prev = head;
  for(let i = 1; i< arr.length;++i){
    const node = new Node(arr[i]);
    prev.next = node;
    prev = node;
    
  }

  return head;
}

  //Tortoise hare implementation
function middleElement(head){

  let fast = head;
  let slow = head;

  let count = 0;
  let increment = 1;
  while(fast.next !== null){
    ++count;
    fast = fast.next;

    if(count === increment){
      slow = slow.next;
      increment += 1;
      count = 0;
    }
  }

  if(count % 2 === 0){
    return slow.next;
  }
  return slow;
}
