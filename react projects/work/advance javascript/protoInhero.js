let pet={
    eats:true
};
let dog={
    jumps:true
};
// let pet={
//     climbs:false
// };
dog.proto = pet;
alert(dog.eats);
alert(dog.jumps);
 alert(dog.climbs);
