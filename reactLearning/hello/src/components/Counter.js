  
 
  class Counter extends Component {
        constructor(props) {
            super(props)
        
            this.state = {
                 count:0
            }
        }
        increment() {
        //     this.setState(                          //first parameter is a object which sets the state value
        //         {
        //             count: this.state.count +1
        //         },
        //        () => {                                // second parameter is the arrow function where we update the state.count value    
        //             console.log('Callback value' , this.state.count)
        //         } 
        //     )
         
        //  console.log(this.state.count )   

          this.setState(prevState =>({
          count:prevState.count +1
          }))
          console.log(this.state.count)
        }
        incrementFive(){
            this.increment()
            this.increment()
            this.increment()
            this.increment()
            this.increment()
        }
     
     render() {
         return (
             <div>
                 <div>
                      count -{this.state.count} 
                      
                      <button onClick = { ()=> this .incrementFive() } > Increment</button>
                 </div>
                
             </div>
         )
     }
 }
 
 export default Counter
 