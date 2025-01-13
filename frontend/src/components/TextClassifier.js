import React, { useState } from 'react';
import { classifyText } from '../services/api';
import ResultDisplay from './ResultDisplay';
import './TextClassifier.css';

const TextClassifier = () => {
    const [inputText, setInputText] = useState('');
    const [classification, setClassification] = useState(null);
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleClassify = async () => {
        setError('');
        setClassification(null);
        setIsLoading(true);

        try {
            const result = await classifyText(inputText);
            setClassification(result);
        } catch (err) {
            setError(err.message || 'An error occurred during classification');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="text-classifier">
            <div className="input-container">
                <textarea
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Type symptoms or a description for classification..."
                    rows={5}
                    className="input-textarea"
                    aria-label="Enter symptoms or description"
                />
                <button 
                    onClick={handleClassify} 
                    disabled={isLoading || !inputText.trim()} 
                    className={`classify-button ${isLoading ? 'loading' : ''}`}
                >
                    {isLoading ? 'Classifying...' : 'Classify Text'}
                </button>
            </div>
            {isLoading && (
                <div className="loading-animation">
                    <div className="spinner"></div>
                    <p>Analyzing your input...</p>
                </div>
            )}
            {error && (
                <div className="error-message">
                    <p>{error}</p>
                    <button onClick={() => setError('')}>Try Again</button>
                </div>
            )}
            <ResultDisplay classification={classification} />
        </div>
    );
};

export default TextClassifier;

