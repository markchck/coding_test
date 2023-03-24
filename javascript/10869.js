const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
const arr = input.map((elem)=>{
    return Number(elem);
})

console.log(arr[0]+arr[1]);
console.log(arr[0]-arr[1]);
console.log(arr[0]*arr[1]);
console.log(parseInt(arr[0]/arr[1]));
console.log(arr[0]%arr[1]);