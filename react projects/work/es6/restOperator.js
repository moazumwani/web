let displayColors =function(message,...colors){
    console.log(message);
    for(let i in colors){
        console.log(colors[i]);
    }
}
let message ="list of colors"
// displayColors(message,'red');                        //   rest operator
// displayColors(message,'red','blue');
// displayColors(message,'red','blue,green');


let colorArray=['orange','yellow','indigo'];           //spread opeator
displayColors (message,...colorArray)