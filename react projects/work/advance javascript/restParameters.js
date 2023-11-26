function fun(...input){
    let sum=0;
    for(let i of input){
        sum+=1;
    }
    return sum;
}
console.log(fun(1,2));
console.log(fun(1,2,4));
console.log(fun(1,2,4,8));