import { useState, useEffect } from 'react'


// que es el UseEffect, metodos de uso con codigo de ejemplo y como usarlo en codigo, adicionalmente metodo de uso practicos y se puede utilizar para consumir una api?

function App() {
    const [ allUser, setAllUser ] = useState({});
    const [ allTask, setAllTask ] = useState({});


    const getAllUser = async () =>{
      let request = await fetch("http://127.0.0.1:8000/user");
      let response = await request.json();
      return console.log(response)
    }

    getAllUser()


    return(
        <>
        <h1>Hola mundo</h1>
        </>
    )
  }



export default App
