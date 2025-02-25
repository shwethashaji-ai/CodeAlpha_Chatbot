from flask import Flask, request, jsonify
import json
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load FAQ data
with open("faqs.json", "r") as file:
    faqs = json.load(file)["faqs"]

# Extract questions and answers
questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_best_answer(user_query):
    """Find the best-matching answer using cosine similarity."""
    user_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarities.argmax()

    if similarities[0, best_match_index] > 0.2:  # Confidence threshold
        return answers[best_match_index]
    else:
        return "I'm sorry, I don't have an answer for that. Please try another question."

@app.route("/")
def home():
    return "FAQ Chatbot API is running! Use /chat endpoint."

@app.route("/chat", methods=["POST"])
def chat():
    """API endpoint to receive a user query and return an answer."""
    data = request.json
    user_input = data.get("question", "")

    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    answer = get_best_answer(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True, port=5001)

