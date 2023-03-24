const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
const arr = input.map(function(elem){
    return Number(elem);
})
let x = arr[0];
let y = arr[1];
let w = arr[2];
let h = arr[3];

let result = [(w-x), (h-y), x, y];
console.log(Math.min(...result));