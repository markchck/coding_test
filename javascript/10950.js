let input = require("fs").readFileSync('/dev/stdin').toString().split('\n');
for (let i=1; i<=input[0]; i++){
    let numbers = input[i].split(' ');
    let elements=numbers.map(function(elem){
        return Number(elem);
    })
    console.log(elements[0]+elements[1]);
}