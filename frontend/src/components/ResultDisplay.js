import React from 'react';

function ResultDisplay({ result }) {
    return (
        <div className="result-display">
            <h3>Classification Result:</h3>
            <p>{result}</p>
        </div>
    );
}

export default ResultDisplay;
