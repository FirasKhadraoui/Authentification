import React from 'react';

const Home = (props) => {
    return (
        <div>
            {/* {props.name ? 'Hi ' + props.name : 'You are not logged in'} */}
            
           Hi {props.name}
        </div>
    );
};

export default Home;