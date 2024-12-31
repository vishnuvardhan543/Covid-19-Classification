from flask import Blueprint, request, jsonify
from .models import TextClassifier
from .utils import preprocess_text

main = Blueprint('main', __name__)

# Initialize the classifier
classifier = TextClassifier()

# Route for classifying text
@main.route('/classify', methods=['POST'])
def classify_text():
    data = request.get_json()
    
    # Check if the input data has text
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    # Preprocess the text (optional step depending on your preprocessing logic)
    preprocessed_text = preprocess_text(text)
    
    # Get classification result from the model
    classification = classifier.predict(preprocessed_text)

    return jsonify({'classification': classification})

# Route for training the model
@main.route('/train', methods=['POST'])
def train_model():
    classifier.train()
    return jsonify({'message': 'Model trained successfully'})
