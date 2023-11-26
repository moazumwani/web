 var getRegvalue = function(){
     return 10;
 }
 console.log(getRegvalue());          
   //arrow function

   const getArrowval =() => {
       return 10;

   }
   console.log(getArrowval());

//    if our func has just single statment within the body
const getArrowvalue =(m) =>  10*m;

console.log(getArrowval(5));

// another short form 
// const getArrowvalue = m =>  10;

// console.log(getArrowval(5));