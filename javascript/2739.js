const input = require('fs').readFileSync('/dev/stdin').toString();
let N = (Number(input));

for (let i=1; i<=9; i++){
    console.log(`${N} * ${i} = ${N*i}`);
}