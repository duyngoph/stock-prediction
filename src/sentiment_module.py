from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_sentiment(texts):
    results = sentiment_pipeline(texts)
    score = 0
    for r in results:
        if r['label'] == 'positive':
            score += 1
        elif r['label'] == 'negative':
            score -= 1
    return score / len(results)