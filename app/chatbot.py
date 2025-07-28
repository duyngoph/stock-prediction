import streamlit as st
from src.predict import run_pipeline

st.title("📈 S&P 500 Movement Predictor")
news_input = st.text_area("Paste today's major financial news headlines (one per line):")

if st.button("Predict Tomorrow's Movement"):
    headlines = news_input.strip().split("\n")
    result, features = run_pipeline(headlines)

    st.write(f"🔮 Prediction: {'UP' if result == 1 else 'DOWN'}")
    st.write("📊 Breakdown:")
    st.json(features)