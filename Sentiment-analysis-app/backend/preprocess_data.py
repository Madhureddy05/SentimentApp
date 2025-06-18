import pandas as pd
import os

folder_path = r"C:\Users\kamir\Desktop\Sentiment-analysis-app\data"
all_files = os.listdir(folder_path)
data_list = []

for filename in all_files:
    if filename.endswith('.txt'):  
        file_path = os.path.join(folder_path, filename)
        with open(file_path, encoding='latin-1') as f:
            text = f.read()
            data_list.append({'filename': filename, 'text': text})

data = pd.DataFrame(data_list)

data.to_csv('processed_sentiment140.csv', index=False)

print("Preprocessing complete. Data saved as 'processed_sentiment140.csv'")
