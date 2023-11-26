import './App.css';
import Greet from './components/Greet'
import Welcome from './components/welcome'
import Hello from './components/hello'
import Message from './components/Message';
import Header from './MyComponents/Headers';
import {Footer} from './MyComponents/Footer';
import {Todos} from './MyComponents/Todos';
import {AddTodo} from './MyComponents/AddTodo';
import React,{useEffect, useState} from 'react';
// import {TodoItem} from './MyComponents/TodoItem';
// import { Chart } from 'chart.js';
// import MyChart from './MyComponents/MyChart';

function App() {
let initTodo;
if (localStorage.getItem("todos")===null){
  initTodo =[];
}
else{
  initTodo=JSON.parse(localStorage.getItem("todos"))
}




  const onDelete=(todo)=>{
    console.log("I am onDelete",todo)
    setTodos (todos.filter((e)=>{
      return e!==todo;
    }));
    localStorage.setItem("todos",JSON.stringify(todos));
  }
  const addTodo =(title,desc)=>{
    console.log("I am adding this toDo",title,desc)
    let sno;
    if(todos.length==0){
      sno=1;
    }
    else{
      sno=todos[todos.length-1].sno+1;
    }
    const myTodo={
      sno:sno,
      title:title,
      desc:desc,
    }
    setTodos([...todos, myTodo])
    console.log(myTodo);
    
  }
    
  // const[todos,setTodos]=useState( [
  //   {
  //     sno: 1,
  //     title:"go to the market",
  //     desc:"we should go to the market to get job 1 done "
  //   },
  //   {
  //     sno: 2,
  //     title:"go to the mall",
  //     desc:"we should go to the market to get job 2 done "
  //   },
  //   {
  //     sno: 3,
  //     title:"go to the ghat",
  //     desc:"we should go to the market to get job 3 done "
  //   },
  //  ]);   sample case of todos now in the next useState we will take the todos from the user and save them as well

  const[todos,setTodos]=useState(initTodo);
  useEffect(() => {
    localStorage.setItem("todos",JSON.stringify(todos));
  
  }, [todos])
  




  return (
    <div className="App">
    <Header title="My Todos list" />
    <AddTodo addTodo ={addTodo}/>
     
     <Todos todos={todos} onDelete={onDelete}/>
     {/* <TodoItem/> */}
     <Footer/>
     {/* <MyChart/> */}





     {/* <Greet name ="mmw" heroName="ironman">
     <p>this is the children prope</p>
     </Greet>
     <Greet name ="moazum" heroName="captain america">
      <button>Actionnnn</button>
      </Greet>
     <Greet name ="aatif" heroName="thor"/> */}
     
     {/* <Welcome/> */}
     {/* <Hello/> */}
     {/* <Message/> */}

    
     


     

    







    </div>
  );
}

export default App;
