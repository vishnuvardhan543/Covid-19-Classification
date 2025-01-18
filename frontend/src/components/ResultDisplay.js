import React from 'react';
import './ResultDisplay.css';

const ResultDisplay = ({ classification }) => {
    if (!classification) return null;

    const getConfidenceColor = (confidence) => {
        if (confidence >= 0.8) return 'high-confidence';
        if (confidence >= 0.6) return 'medium-confidence';
        return 'low-confidence';
    };

    return (
        <div className="result-display">
            <h3>Classification Result</h3>
            <div className={`result-content ${getConfidenceColor(classification.confidence)}`}>
                <div className="classification-box">
                    <p className="classification">{classification.classification}</p>
                    {/* {!isNaN(classification.confidence) && (
                        <p className="confidence">
                            Confidence: {(classification.confidence * 100).toFixed(2)}%
                        </p>
                    )} */}
                </div>
            </div>
        </div>
    );
};

export default ResultDisplay;

