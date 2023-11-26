let user={
    firstname:"moazum"
};
function func(){
    alert(this.firstname);
}
let funcUser= func.bind(user);
funcUser();