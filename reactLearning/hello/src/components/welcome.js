 import React,{Component} from 'react'

//  class Welcome extends Component{
//    render(){
//        return <h1>Welcome {this.props.name} a.k.a {this.props.heroName} </h1>
//    } 
//  }
//  export default Welcome

 // destruct props in class

 class Welcome extends Component{
  render(){
    const{name ,heroName} =this.props
    //const{ state1,state2} =this.state        //code for different states
      return <h1>Welcome {name} a.k.a {heroName} </h1> 
  } 
}
export default Welcome