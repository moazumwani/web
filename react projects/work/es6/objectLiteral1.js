let firstname ="chandler";
let lastname ="bing";

let person={
    firstname,
    lastname
};
// console.log(person.firstname);
// console.log(person.lastname);



function createPerson(firstname,lastname,age){
    let fullname = firstname + " " +lastname;
    return{firstname,
        lastname,
        fullname,
           isSenior(){
               return age>60;
           }
    } 
}
let p =createPerson("ross","geller",72);
console.log(p.firstname);
console.log(p.lastname);
console.log(p.fullname);
console.log(p.isSenior());