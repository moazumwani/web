import React from 'react'
// function Greet(){
//     return <h1>hello moazum</h1>
// }
const Greet = props =>{
  console.log(props)
  return (
           <div>
                <h1>
                     hello {props.name} a.k.a {props.heroName}
                     </h1>
               {props.children}
           </div>

  ) 
} 
export default Greet


//destruction in props methos 1 destructimg in the parameter

// const Greet = ({name,heroName}) =>{
  
//   return (
//            <div>
//                 <h1>
//                      hello {name} a.k.a {heroName}
//                      </h1>
               
//            </div>

//   ) 
// } 
//  export default Greet


//destructure in the function body


// const Greet = props =>{
//   const {name, heroName} =props
//   return (
//            <div>
//                 <h1>
//                      hello {name} a.k.a {heroName}
//                      </h1>
               
//            </div>

//   ) 
// } 
// export default Greet
