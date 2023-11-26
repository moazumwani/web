let perbonus=()=>0.1;
let getValue =function(value=10 ,bonus=value*perbonus()){
    console.log(value+bonus);

};
getValue();
getValue(20);
getValue(20,30);