import React,{Component} from 'react'

class Message extends Component{
  constructor(){
    super()
    this.state={
      messgae:'welcome visitor'
    }
  }
  changeMessage(){
    this.setState({
      messgae:'Thank you for Subscribing'
    })
  }
  render(){
      return(
        <div>
            <h1>{this.state.messgae}</h1>
            <button onClick={() => this.changeMessage()}>Subscribe</button>
        </div>
      ) 
  } 
}
export default Message