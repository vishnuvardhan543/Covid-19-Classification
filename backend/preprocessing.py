import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Function to load and preprocess the data
def load_and_preprocess_data(csv_file):
    # Load the dataset
    df = pd.read_csv(csv_file)

    # Keep the relevant columns
    df = df[['clinical_notes', 'finding']]

    # Handle missing values if any
    df = df.dropna()

    # Convert clinical_notes to text data and finding to labels
    text_data = df['clinical_notes']
    labels = df['finding']

    return text_data, labels

# Function to encode the labels (e.g., 'Pneumonia/Viral/COVID-19' etc.)
def encode_labels(labels):
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)
    return labels_encoded, label_encoder

# Function for TF-IDF Vectorization
def vectorize_text_data(text_data):
    tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X = tfidf_vectorizer.fit_transform(text_data)
    return X, tfidf_vectorizer

# Function to split data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
