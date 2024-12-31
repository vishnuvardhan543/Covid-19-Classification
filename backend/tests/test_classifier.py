import unittest
from app.models import TextClassifier
from app.utils import preprocess_text

class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = TextClassifier()
        self.classifier.train()

    def test_preprocessing(self):
        text = "Patient with COVID-19 symptoms: fever, cough, and shortness of breath."
        processed = preprocess_text(text)
        self.assertIn('fever', processed)
        self.assertIn('cough', processed)
        self.assertNotIn('with', processed)

    def test_classification(self):
        covid_text = "Patient experiencing severe respiratory symptoms, high fever, and loss of taste."
        sars_text = "Patient with SARS showing signs of atypical pneumonia and rapid onset of fever."
        ards_text = "Patient diagnosed with ARDS, presenting with severe breathlessness and bilateral infiltrates on chest X-ray."

        self.assertEqual(self.classifier.predict(covid_text), 'COVID')
        self.assertEqual(self.classifier.predict(sars_text), 'SARS')
        self.assertEqual(self.classifier.predict(ards_text), 'ARDS')

if __name__ == '__main__':
    unittest.main()