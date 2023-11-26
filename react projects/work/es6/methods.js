class Person {
    constructor(name) {             // constructor method
        this.name = name;
        console.log(this.name + "constructor");
    }
    static staticMethod() {
        console.log("Static method");
    }
    greetPerson(){
     console.log("hello" + this.name);          //proptype method   
    }
}
let p = new Person("chandler");      //constructor method
Person.staticMethod();    // static method
p.greetPerson();