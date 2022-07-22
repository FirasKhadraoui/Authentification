import React from 'react'
import { Link } from 'react-router-dom'

const Nav = (props) => {
    const logout = async () => {
        await fetch('http://localhost:8000/app/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
        });

        props.setName('');
    }

return (
    <div>
        <nav className="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <div className="container-fluid">
                <Link to="/" className="navbar-brand">Home</Link>

                <div>
                {props.name?(
                     <ul className="navbar-nav me-auto mb-2 mb-md-0">
                     <li className="nav-item">
                     <Link to="/login" className="nav-link" onClick={logout}>Logout</Link>
                     </li>
                 </ul>
                ):(
                    <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item">
                    <Link to="/login" className="nav-link active" aria-current="page">Login</Link>
                </li>
                <li className="nav-item">
                    <Link to="/register" className="nav-link active" aria-current="page">Register</Link>
                </li>
            </ul>
                )
                
            }
                </div>
            </div>
        </nav>
    </div>
);
};
export default Nav;