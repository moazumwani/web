let myMap =new Map();
myMap.set("fname" , "chandler"); // with bracket we specify key and value key is fname and value is chandler
myMap.set("age",30);


console.log(myMap.get("fname"));

let ob1={};
let ob2 ={};


myMap.set(ob1,10);
myMap.set(ob2,20);

console.log(myMap.get(ob1));
console.log(myMap.size);
console.log(myMap.has("fname"));