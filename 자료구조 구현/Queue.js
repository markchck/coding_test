class Queue {
    constructor(){
        this.queue = []
    }
    enqueue(value){
        this.queue.push(value);
    }
    
    dequeue(){
        let popleft = this.queue[0]
        this.queue = this.queue.slice(1)
        return popleft
    }
}

que =new Queue()
que.enqueue(1);
que.enqueue(2);
que.enqueue(3);
que.enqueue(4);
console.log(que.dequeue());
console.log(que.queue);