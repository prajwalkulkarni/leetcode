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


// Delete Nth node from the last
const header = createDLL();

//Brute force approach
// Find the length of the LL, and call it L, Nth node from behind is L - N th from ahead with 0 - index

function deleteNode(n, head){
  let curr = head;
  let l = 0;
  while(curr.next !== null){
    l+=1;
  }

  const target = l - n;
  let currentIndex = 0;
  curr = head;
  while(currentIndex < target - 1){
    currentIndex += 1;
    curr = curr.next;
  }
  const targetNode = curr.next.next;
  curr.next = targetNode;
  targetNode.next = null
  
  
}
