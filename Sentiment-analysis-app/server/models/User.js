const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String },
  googleId: { type: String }, // For OAuth Google Login
  history: [
    {
      text: String,
      sentiment: String,
      date: { type: Date, default: Date.now }
    }
  ],
});

module.exports = mongoose.model('User', userSchema);
