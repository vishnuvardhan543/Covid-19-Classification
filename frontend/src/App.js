import React from 'react';
import Header from './components/Header';
import TextClassifier from './components/TextClassifier';
import Footer from './components/Footer';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <div className="background-gradient"></div>
      <Header />
      <main className="main-content">
        <TextClassifier />
      </main>
      <Footer />
    </div>
  );
};

export default App;

