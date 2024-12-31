// App.js
import React from 'react';
import './App.css';
import TextClassifier from './components/TextClassifier';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>COVID-19 Text Classification</h1>
      </header>
      <main>
        <TextClassifier />  {/* Render TextClassifier component */}
      </main>
    </div>
  );
}

export default App;
