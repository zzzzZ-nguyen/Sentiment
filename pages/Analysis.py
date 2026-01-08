import streamlit as st
import joblib
import json
import re

# Load English model
log_reg = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load Vietnamese dictionary
with open("models/vi_dictionary.json", "r", encoding="utf-8") as f:
    vi_dict = json.load(f)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ỹ\s]", "", text)
    return text

def predict_en(text):
    vec = vectorizer.transform([text])
    pred = log_reg.predict(vec)[0]
    prob = max(log_reg.predict_proba(vec)[0])
    return pred, prob

def predict_vi(text):
    score = 0
    for word in vi_dict["positive"]:
        if word in text: score += 1
    for word in vi_dict["negative"]:
        if word in text: score -= 1

    if score > 0: return "Positive", 1.0
    elif score < 0: return "Negative", 1.0
    else: return "Neutral", 1.0

def show():
    st.markdown("## 🔎 Sentiment Analysis")
    user_input = st.text_area("Nhập câu đánh giá sản phẩm:")

    if st.button("Phân tích"):
        text = preprocess_text(user_input)

        if re.search(r"[a-zA-Z]", text):  # English
            label, conf = predict_en(text)
        else:  # Vietnamese
            label, conf = predict_vi(text)

        st.success(f"👉 Kết quả: **{label}** (Confidence: {conf:.2f})")
