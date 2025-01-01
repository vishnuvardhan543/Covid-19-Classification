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
                    placeholder="Enter text related to COVID-19 to classify..."
                    rows={5}
                    className="input-textarea"
                />
                <button onClick={handleClassify} disabled={isLoading || !inputText.trim()} className="classify-button">
                    {isLoading ? 'Analyzing...' : 'Classify Text'}
                </button>
            </div>
            {error && <p className="error-message">{error}</p>}
            <ResultDisplay classification={classification} />
        </div>
    );
};

export default TextClassifier;

