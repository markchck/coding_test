// const input = Number(require('fs').readFileSync('/dev/stdin').toString());
// function f1(input){
//     if ((input%4 ===0 && input%100 !==0) || (input%400 === 0)){
//         return 1;
//     }else{
//         return 0;
//     }
// }

// console.log(f1(input));


const input = Number(require('fs').readFileSync('/dev/stdin').toString());

if ((input%4 ===0 && input%100 !==0) || (input%400 === 0)){
    console.log(1);
}else{
    console.log(0);
}