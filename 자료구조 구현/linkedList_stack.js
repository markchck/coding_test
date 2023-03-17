class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.size = 0;
  }

  push(value) {
    const newNode = new Node(value);
    newNode.next = this.top;
    this.top = newNode;
    this.size++;
  }

  pop() {
    if (this.top === null){
        return null;
    }
    let tmp = this.top.value;
    this.top = this.top.next;
    return tmp
  }
  
  contain(value){
    let currentNode = this.top;
    while (currentNode.next !== null){
      if(currentNode.value ===value){
        return true
      }else{
        currentNode = currentNode.next;
      }
    }
    return false
  }

}

let stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.contain(3));
console.log(stack.contain(4));
console.log(stack.pop());
console.log(stack.pop());
