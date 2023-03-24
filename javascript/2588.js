const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const a = parseInt(input[0]);
const b = parseInt(input[1]);



const first = parseInt(b/100);
// const second = parseInt((b%(first*100))/10);
const second = parseInt(b/10)%10;
const third =  parseInt(b%(first*100 + second*10));

console.log(a*third);
console.log(a*second);
console.log(a*first);
console.log(a*b);