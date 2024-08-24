// Reverse a doubly linked list


class Node{

  constructor(val, next = null, prev = null){
    this.val = val;
    this.prev = prev;
    this.next = next;
  }
}


function createDLL(){
  let arr= [1,2,3,4,5,6,7,8,9];

const head = new Node(arr[0])
let curr = head;
for(let i = 1;i<arr.length; ++i){
  const node = new Node(arr[i]);
  node.prev = curr;
  curr.next = node;
  curr = node;
}

curr = head;

while(curr.next !== null){
  console.log(curr.val);
  curr = curr.next;
}
return head;
}

function reverse(head){
  let temp = null;
  while (current != null) {
            temp = current.prev;
            current.prev = current.next;
            current.next = temp;
            current = current.prev;
  }
  console.log(curr);

  
}
