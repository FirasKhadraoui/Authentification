import React, { useState } from 'react';
import {Navigate} from 'react-router-dom';

const Register = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false);

    const submit = async (e) => {
        e.preventDefault();
        console.log({
            name,
            email,
            password
        })

        // const response = await fetch("http://localhost:8000/app/register")
        await fetch('http://localhost:8000/app/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                name,
                email,
                password
            })
        });
        setRedirect(true);
    }
    if (redirect) {
        return <Navigate to="/login"/>;
    }
    return (
        <div>
            <form onSubmit={submit}>
                <h1 className="h3 mb-3 fw-normal">Please register</h1>
                <div className="form-floating">
                    <input type="text" className="form-control" id="floatingInput" placeholder="Name"
                        required onChange={e => setName(e.target.value)} />
                    <label for="floatingInput">Name</label>
                </div>
                <div className="form-floating">
                    <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                        required onChange={e => setEmail(e.target.value)} />
                    <label for="floatingInput">Email address</label>
                </div>
                <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                        required onChange={e => setPassword(e.target.value)} />
                    <label for="floatingPassword">Password</label>
                </div>

                <div className="checkbox mb-3">
                </div>
                <button className="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Register;