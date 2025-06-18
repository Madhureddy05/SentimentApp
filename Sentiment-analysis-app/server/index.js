const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const axios = require('axios');

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/analyze', async (req, res) => {
    const { text } = req.body;
    if (!text) return res.status(400).json({ error: 'Text is required' });

    try {
        const response = await axios.post('https://sentimentapp-zem2.onrender.com/predict', { text });
        const sentiment = response.data.sentiment;

        res.json({ sentiment });
    } catch (error) {
        console.error("Error in analyzing sentiment:", error);  // Log the full error here
        res.status(500).json({ error: 'Error predicting sentiment' });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
