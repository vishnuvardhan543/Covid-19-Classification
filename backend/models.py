import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from .utils import preprocess_text

class TextClassifier:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000)),
            ('clf', MultinomialNB()),
        ])
        self.trained = False

    def train(self):
        # Get the absolute path to the 'clinical_reports.csv' file in the 'data' folder
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'clinical_reports.csv')
        
        # Read the CSV file
        data = pd.read_csv(data_path)
        print(f"Loaded data with {len(data)} rows.")  # Check how many rows are there
        print(data.head())  # Print the first few rows to see if the data is correct
        
        # Check if the columns 'clinical_notes' and 'finding' exist
        if 'clinical_notes' not in data.columns or 'finding' not in data.columns:
            print("Missing 'clinical_notes' or 'finding' column in the data.")
            return
        
        # Handle missing or invalid 'clinical_notes' values by replacing them with empty strings
        data['clinical_notes'] = data['clinical_notes'].fillna('')
        
        # Preprocess text and get features and labels
        X = data['clinical_notes'].apply(lambda x: preprocess_text(str(x)))  # Ensure the data is treated as a string
        y = data['finding']

        # Check for class balance
        print(f"Label distribution: \n{y.value_counts()}")
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(f"Training data size: {len(X_train)}")
        print(f"Testing data size: {len(X_test)}")

        # Train the model
        self.model.fit(X_train, y_train)
        self.trained = True

        # Evaluate the model's accuracy
        accuracy = self.model.score(X_test, y_test)
        print(f"Model trained with accuracy: {accuracy:.2f}")

    def predict(self, text):
        if not self.trained:
            self.train()

        # Make a prediction on the provided text
        prediction = self.model.predict([text])[0]
        return prediction
