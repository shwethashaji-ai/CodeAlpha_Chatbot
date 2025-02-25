# CodeAlpha_Chatbot
# 🤖 FAQ Chatbot API

A simple chatbot that answers frequently asked questions (FAQs) using **Natural Language Processing (NLP)** and **Flask**. It utilizes **TF-IDF vectorization** and **cosine similarity** to find the best-matching response from a predefined FAQ dataset.

---

## 🚀 Features
✅ Answer FAQs using NLP  
✅ Uses **TF-IDF** & **Cosine Similarity** for response matching  
✅ Flask-based API for easy integration  
✅ Simple JSON-based FAQ storage  
✅ Supports **Postman, Curl, or Python requests** for API testing  

---

## 📂 Project Structure

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/shwethashaji-ai/CodeAlpha_Chatbot.git
cd faq-chatbot

2️⃣ Install Dependencies
Make sure you have Python 3.x installed. Then, run:
pip install -r requirements.txt
python -m spacy download en_core_web_sm

3️⃣ Run the Chatbot API
python app.py
It should show:
FAQ Chatbot API is running! Use /chat endpoint.

📡 API Usage

POST /chat
Endpoint: http://127.0.0.1:5000/chat
Request Format (JSON):
{
  "question": "What is your product?"
}
Response (JSON):
{
  "response": "Our product is an AI-powered chatbot for answering FAQs."
}
Test with curl
curl -X POST "http://127.0.0.1:5000/chat" -H "Content-Type: application/json" -d '{"question": "How does it work?"}'
🎯 Future Enhancements

🔹 Improve accuracy using GPT-3.5 or BERT
🔹 Add database support (SQLite, Firebase)
🔹 Build a web interface (React.js/HTML+JS)

💡 Contributing

Feel free to fork this repo and submit a PR! 🚀

📜 License

This project is MIT licensed.

🔗 Connect with Me
📧 Email: shwetha.shaji15@gmail.com
🔗 GitHub: https://github.com/shwethashaji-ai


