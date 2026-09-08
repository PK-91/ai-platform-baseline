from fastapi import FastAPI

app = FastAPI(title="AI Platform Baseline API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")

    if not text:
        return {"error": "text is required"}

    # Simple placeholder model.
    # We will replace this with a real AI/ML model later.
    positive_words = ["good", "great", "love", "excellent", "happy"]
    negative_words = ["bad", "terrible", "hate", "poor", "sad"]

    text_lower = text.lower()

    positive_score = sum(word in text_lower for word in positive_words)
    negative_score = sum(word in text_lower for word in negative_words)

    if positive_score > negative_score:
        prediction = "positive"
    elif negative_score > positive_score:
        prediction = "negative"
    else:
        prediction = "neutral"

    return {
        "input": text,
        "prediction": prediction
    }