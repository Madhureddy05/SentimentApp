
import re

def extract_sentences_and_labels(filename):
    sentences = []
    labels = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
           
            match = re.match(r'\((\d) (.+)\)', line.strip())
            if match:
                label = int(match.group(1))
                text = re.sub(r'\(\d ', '', match.group(2)) 
                text = re.sub(r'[()]', '', text)  
                sentences.append(text.strip())
                labels.append(label)
    
    return sentences, labels

train_sentences, train_labels = extract_sentences_and_labels('train.txt')
test_sentences, test_labels = extract_sentences_and_labels('test.txt')


import pandas as pd
data = pd.DataFrame({
    'text': train_sentences,
    'target': train_labels
})

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
import pickle

X_train, X_test, y_train, y_test = train_test_split(data['text'], data['target'], test_size=0.2, random_state=42)
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
from collections import Counter
print(Counter(train_labels))


print("Model trained and saved as 'sentiment_model.pkl'")
