class Stack {
    constructor(){
        this.items = [];
        this.ptr = 0;
    }

    push(ele){
        let new_stack = [ele];
        this.items = this.items.concat(new_stack);
        this.ptr ++;
        // this.items.push(ele);
    }

    pop(){
        if(this.items.length === 0) return "Underflow";
        else{
            this.ptr --;
            let pop = this.items[this.ptr];
            this.items=this.items.slice(0,this.ptr);
            return pop ;
        }
    }
}

let stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.pop());
console.log(stack.items)
