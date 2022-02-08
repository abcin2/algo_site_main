import './AlgorithmPage.css';

import React, { useState, useEffect } from 'react';


function AlgorithmPage() {

    const [algorithms, setAlgorithms] = useState([]);

    useEffect(() => {
        getAlgorithms()
    }, [])

    let getAlgorithms = async () => {
        let response = await fetch('http://localhost:8000/api/algo_types/')
        let data = await response.json()
        setAlgorithms(data)
    }

    const strToUrl = (type) => {
        let lower = type.toLowerCase();
        let sep_words = lower.split(' ');
        let new_url = sep_words.join('_');
        return new_url
    }

  return (
    <div>
        <h1>Algorithms Visualized</h1>
        <h2 style={{"fontWeight": "200"}}>choose your algorithm</h2>
        <div className='algo-list'>
            {algorithms.map((algo, index) => (
                <div style={{"width": "18rem"}} className="algo-card" key={index} class="card text-left">
                    <img style={{"height": "10rem", "objectFit": "cover"}} class="card-img-top" src={`${algo.algo_thumbnail}`} alt="Card image cap" />
                    <div class="card-body">
                        <h5 class="card-title">{ algo.algo_type }</h5>
                        <p class="card-text">{ algo.algo_description }</p>
                        <a href={`${strToUrl(algo.algo_type)}`} class="btn btn-primary">Visualize!</a>
                    </div>
                </div>
            ))}
        </div>
    </div>
  );
}

export default AlgorithmPage;
