import React, { useState } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const analyzeSentiment = async () => {
    if (!text.trim()) {
      setResult('Please enter text to analyze.');
      return;
    }
    setLoading(true);
    setResult('');

    try {
      const response = await axios.post('https://sentimentapp-1.onrender.com/api/analyze', { text });
      setResult(response.data.sentiment);
    } catch (error) {
      console.error("Error analyzing sentiment:", error);
      setResult('Error analyzing sentiment');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-blue-100 to-blue-200">
      <div className="bg-white p-8 rounded-2xl shadow-lg max-w-lg w-full space-y-6">
        <motion.h1 className="text-4xl font-bold text-center text-gray-800" initial={{ scale: 0.9 }} animate={{ scale: 1 }}>
          Sentiment Analysis
        </motion.h1>
        <textarea
          placeholder="Enter text to analyze..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="w-full p-4 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          rows="4"
        />
        <button
  onClick={analyzeSentiment}
  className="w-full px-4 py-2 bg-gray-800 text-white rounded-md font-semibold hover:bg-gray-900 transition"
  disabled={loading || !text.trim()}
>
  {loading ? 'Analyzing...' : 'Analyze Sentiment'}
</button>

        {result && (
          <motion.div 
            initial={{ opacity: 0 }} 
            animate={{ opacity: 1 }} 
            className={`p-4 text-white text-center rounded-md ${
              result === 'Positive' ? 'bg-green-500' :
              result === 'Negative' ? 'bg-red-500' : 'bg-yellow-500'
            }`}
          >
            Sentiment: {result}
          </motion.div>
        )}
      </div>
    </div>
  );
}

export default App;
