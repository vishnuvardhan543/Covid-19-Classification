import React, { useState } from 'react';
import { classifyText } from '../services/api';
import ResultDisplay from './ResultDisplay';

const TextClassifier = () => {
    const [inputText, setInputText] = useState('');
    const [classification, setClassification] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleClassify = async () => {
        setError('');
        setClassification('');
        setIsLoading(true);

        try {
            const result = await classifyText(inputText);
            setClassification(result.classification);
        } catch (err) {
            setError(err.message || 'An error occurred during classification');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="text-classifier">
            <textarea
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter text to classify"
                rows={5}
                className="input-textarea"
            />
            <button onClick={handleClassify} disabled={isLoading} className="classify-button">
                {isLoading ? 'Classifying...' : 'Classify'}
            </button>
            {error && <p className="error-message">{error}</p>}
            <ResultDisplay classification={classification} />
        </div>
    );
};

export default TextClassifier;

