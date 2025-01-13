import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(csv_file):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        raise Exception(f"File not found: {csv_file}")

    if 'clinical_notes' not in df.columns or 'finding' not in df.columns:
        raise Exception("Required columns not found in the CSV file.")

    df = df[['clinical_notes', 'finding']].dropna()

    text_data = df['clinical_notes']
    labels = df['finding']

    return text_data, labels

def encode_labels(labels):
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)
    return labels_encoded, label_encoder

def vectorize_text_data(text_data):
    tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X = tfidf_vectorizer.fit_transform(text_data)
    return X, tfidf_vectorizer

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)