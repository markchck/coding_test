class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack{
    constructor(){
        this.top = null;
    }
    push(value) {
        let node = new Node(value);
        node.next = this.top;
        this.top = node;
    }
    pop(){
        let tmp = this.top.value;
        this.top = this.top.next;
        return tmp
    }
    contain(value){
        let current=this.top
        while(current.next !== null){
            if(current.value === value){
                return true;
            }else{
                current = current.next;
            }
        }
        return false;
    }

    print(){
        let current=this.top
        while (current.next !== null){
            console.log(current.value);
            current = current.next;
        }
        console.log(current.value);
    }
}

let stack = new Stack();
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
console.log(stack.contain(5));
stack.print()
