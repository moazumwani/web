class Person{
    constructor (name){
        console.log(name + "person constructor")
    }
    getID(){
        return 10;
    }
}
class Employee extends Person{
constructor(name){
    super(name);
    console.log(name + "enplyee constructod");
}
// getID(){
//     return 50; //it will return this  not parents return 
// }
getID(){
    return super.getID();   // will return parents 
}

}
let e = new Employee("chandler");
console.log();