import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from .utils import preprocess_text

class TextClassifier:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000)),
            ('clf', MultinomialNB()),
        ])
        self.trained = False
        self.model_path = 'model.pkl'  # Path to save/load the model
        self.load_model()  # Load the model if available, else train it

    def load_model(self):
        # Load the model if it exists
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            self.trained = True
        else:
            # If no model is found, train the model automatically
            print("No pre-trained model found. Training the model now...")
            self.train()

    def save_model(self):
        # Save the trained model to a file
        joblib.dump(self.model, self.model_path)

    def train(self):
        # Load and preprocess the training data
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'clinical_reports.csv')
        
        try:
            data = pd.read_csv(data_path)
        except FileNotFoundError:
            raise Exception("Training data file not found.")
        
        if 'clinical_notes' not in data.columns or 'finding' not in data.columns:
            raise Exception("Required columns not found in the training data.")
        
        data['clinical_notes'] = data['clinical_notes'].fillna('')
        
        X = data['clinical_notes'].apply(lambda x: preprocess_text(str(x)))
        y = data['finding']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        self.model.fit(X_train, y_train)
        self.trained = True
        
        # Save the model to disk
        self.save_model()

        accuracy = self.model.score(X_test, y_test)
        print(f'Model trained with accuracy: {accuracy * 100:.2f}%')
        return accuracy

    def predict(self, text):
        if not self.trained:
            raise Exception("Model not trained. Please train the model first.")

        prediction = self.model.predict([text])[0]
        confidence = np.max(self.model.predict_proba([text]))
        return prediction, float(confidence)
