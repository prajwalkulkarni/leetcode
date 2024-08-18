// DLL


const arr = [1,2,3,4,5,6,7,8]


class Node{
  constructor(data, next = null, prev = null){

    this.data = data;
    this.next = next;
    this.prev = prev;
  }
}

function arrayToDoublyLinkedList(arr){

  const head = new Node(arr[0]);
  let temp = head;
  for(let i = 1;i<n;++i){

    const node = new Node(arr[i]);

    node.prev = temp;
    temp.next = node;
    temp = node;
  }

  return head;
}


//Insert node at the tail of a DLL

function insertNodeAtTail(head, value){

  let curr = head;

  while(curr.next !== null){
    curr = curr.next;
  }

  const newNode = new Node(value);

  curr.next = newNode;

  return head
}

// Delete a node at Nth position in a DLL;

function deleteNode(head,position){

  let count = 0;
  let curr = head;

  while(curr){
    curr = curr.next
    ++count;
  }

  if(position > count - 1){
    throw new Error("Index out of bounds exception")
  }

  let currentPos = 0;
  curr = head;
  let prev = head;

  while(currentPos<position){
    ++currentPos;
    prev = curr;
    curr = curr.next;
  }

  prev.next = curr.next
  curr.next.prev = prev;
  curr.next = null;
  curr.prev = null;

  return head;
}
