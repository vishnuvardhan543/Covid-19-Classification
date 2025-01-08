import nltk
from flask import Blueprint, request, jsonify
from .models import TextClassifier
from .utils import preprocess_text

# Ensure necessary NLTK resources are downloaded only once
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

# Initialize the blueprint and classifier
main = Blueprint('main', __name__)
classifier = TextClassifier()

@main.route('/classify', methods=['POST'])
def classify_text():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'text' key exists in the incoming data
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    
    try:
        # Preprocess the input text
        preprocessed_text = preprocess_text(text)

        # Get prediction and confidence from the classifier
        classification, confidence = classifier.predict(preprocessed_text)
        
        # Return the classification and confidence as a response
        return jsonify({
            'classification': classification,
            'confidence': confidence
        })
    
    except Exception as e:
        # Log the error and return a 500 error response
        print(f"Error during classification: {e}")
        return jsonify({'error': str(e)}), 500

@main.route('/train', methods=['POST'])
def train_model():
    try:
        # Train the model
        accuracy = classifier.train()
        
        # Return success message with accuracy
        return jsonify({
            'message': 'Model trained successfully',
            'accuracy': accuracy
        })
    
    except Exception as e:
        # Log the error and return a 500 error response
        print(f"Error during model training: {e}")
        return jsonify({'error': str(e)}), 500
