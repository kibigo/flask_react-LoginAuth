import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Form} from 'react-bootstrap'
import { Link } from "react-router-dom";


function LandingPage (){

    return(
        <div>
            <h1>Welcome</h1>
            <p>You are not logged in</p>

            <Form>
                <Link to='/login'>
                    <Button className="btn btn-success">Login</Button>
                </Link>
                &nbsp;
                <Link to='/register'>
                    <Button className="btn btn-danger">Register</Button>
                </Link>
            </Form>
        </div>
    )
}

export default LandingPage