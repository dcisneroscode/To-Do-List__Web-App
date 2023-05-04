import { createContext } from "react";
import { useContext } from "react";
import { useEffect, useState } from "react";


const CreateContextApp = createContext()


function AppContext(){
    const [ allUser, setAllUser ] = useState({});
    const [ allTask, setAllTask ] = useState({});

    useEffect(() =>{

        const getAllUser = async () =>{
            let request = await fetch("http://127.0.0.1:8000/user");
            let response = await request.json()
            let data = setAllUser({response})
        }



    })

    return(
        <>
        <h1>{setAllUser}</h1>
        </>
    )

}

export { AppContext }