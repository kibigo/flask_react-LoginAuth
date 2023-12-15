import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";
import { useNavigate } from "react-router-dom";


function Login() {
    
    const [formData, setFormData] = useState({
        email:'',
        password:''
    })

    const handleChange = (event) => {
        const key = event.target.id
        const value = event.target.value
        setFormData({...formData, [key]: value})
    }

    const objBody = {
        email: formData.email,
        password: formData.password
    }

    const navigate = useNavigate()

    const logInUser = (e) => {
        e.preventDefault()
        fetch('http://127.0.0.1:5000/login', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(objBody)
        })
        .then((response) => {
            response.json()
            
            if (response.status == 200){
                navigate('/')
            } else if(response.status == 401){
                console.log('Invalid credentials')
            }
        })
        .catch((error) => {
            console.log('This is the error: ', error)
        })

    }

    const formstyle = {
        display: 'flex',
        flexDirection:'column',
        alignItems:'center',
        margin:'70px auto',
        backgroundColor:'#2C5F2D',
        height:'50vh',
        justifyContent:'center',
        width:'40%',
        borderRadius:'10px'

    }

    const inputStyle = {
        width:'100%',
        borderRadius:'15px',
        border:'1px solid black',
        padding:'10px',
        marginTop:'15px'

    }
    
    const buttonStyle = {
        borderRadius:'10px',
        width:'40%',
        marginTop:'10px'
        
    }

    return (
        <div>
            <Form style={formstyle}>
                <h1>Log into your account</h1>
                <Form.Group>
                    <Form.Control style={inputStyle} onChange={handleChange} type="email" placeholder="email" id="email" value={formData.email}/>
                </Form.Group>

                <Form.Group>
                    <Form.Control style={inputStyle} onChange={handleChange} type="password" placeholder="password" id="password" value={formData.password}/>
                </Form.Group>

                <Button onClick={logInUser} type="submit" style={buttonStyle}>Login</Button>
            </Form>
        </div>

    )
}

export default Login