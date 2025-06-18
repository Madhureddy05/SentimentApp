from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
print("Loaded URI:", os.getenv("MONGO_URI"))
client = MongoClient(os.getenv("MONGO_URI"))  
db = client.sentimentApp
collection = db.analysis

app = Flask(__name__)
CORS(app) 

with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Text is required"}), 400

    prediction = model.predict([text])[0]
    print(f"Predicted Label: {prediction}")  

    if prediction in [3, 4]:
        sentiment = "Positive"
    elif prediction in [1, 2]:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    try:
        collection.insert_one({
        "text": text,
        "prediction": int(prediction),
        "sentiment": sentiment,
        "timestamp": datetime.utcnow()
    })
        print("Data inserted into MongoDB")
    except Exception as e:
        print("MongoDB insert failed:", e)

    return jsonify({
        "sentiment": sentiment,
        "label": int(prediction)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pickle

# app = Flask(__name__)
# CORS(app)  # Enables CORS for all routes

# # Load the trained sentiment analysis model
# with open('sentiment_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     text = data.get("text", "").strip()

#     if not text:
#         return jsonify({"error": "Text is required"}), 400

#     prediction = model.predict([text])[0]
#     print(f"Predicted Label: {prediction}")  # Add this line

#     if prediction in [3, 4]:
#         sentiment = "Positive"
#     elif prediction in [1, 2]:
#         sentiment = "Neutral"
#     else:
#         sentiment = "Negative"

#     return jsonify({
#         "sentiment": sentiment,
#         "label": int(prediction)
#     })


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)
