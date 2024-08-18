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



// Insert new head to LL



const currHead = arrayToLinkedList(arr)

const newHead = new Node(0);
newHead.next = currHead;


//Delete tail in a LL

function deleteTail(arr){

  const head = arrayToLinkedList(arr);

  let prev = head;
  let curr = head;

  while(curr.next !== null){
    prev = curr;
    curr = curr.next
  }

  prev.next = null;
  
}

//Get length of LL

function getLength(head){

  let count = 0;
  let curr = head;

  while(curr.next !== null){
    count+=1;
    curr = curr.next
  }

  return count + 1;
}


//Search an element in a linked list

function searchElement(head, item){

  let temp = head;

  while(temp.next){
    if(temp.data === item){
      return 1;
    }

    temp = temp.next;
  
  }

  return 0;
}
