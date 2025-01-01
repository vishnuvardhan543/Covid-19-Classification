import React from 'react';
import './App.css';
import TextClassifier from './components/TextClassifier';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>COVID-19 Text Classification</h1>
        <p>Analyze text related to COVID-19 for instant, AI-powered insights</p>
      </header>
      <main className="App-main">
        <TextClassifier />
      </main>
      <footer className="App-footer">
        <p>&copy; 2024 COVID-19 Text Classification Project | Stay Safe, Stay Informed</p>
      </footer>
    </div>
  );
}

export default App;
