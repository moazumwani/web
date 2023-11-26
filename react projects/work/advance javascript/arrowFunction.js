 hello= ()=>{
     document.getElementById("demo").innerHTML +=this;
 }
//  window object calls the function 
window.addEventListener("load",hello);
//  button object calls func
document.getElementById("btn").addEventListener("click",helo);