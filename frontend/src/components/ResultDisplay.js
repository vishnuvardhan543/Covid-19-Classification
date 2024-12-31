// ResultDisplay.js
import React from 'react';

const ResultDisplay = ({ classification }) => {
    return (
        <div>
            <h3>Classification Result:</h3>
            {classification ? <p>{classification}</p> : <p>No classification available</p>}
        </div>
    );
};

export default ResultDisplay;
