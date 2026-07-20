from textblob import TextBlob


# -----------------------------------
# Sentiment Analysis
# -----------------------------------
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"


# -----------------------------------
# Complaint Category Detection
# -----------------------------------
def detect_category(text):
    text = text.lower()

    categories = {
        "Billing": [
            "bill",
            "billing",
            "payment",
            "refund",
            "charge",
            "invoice"
        ],
        "Technical": [
            "error",
            "bug",
            "crash",
            "login",
            "server",
            "website",
            "app",
            "technical"
        ],
        "Delivery": [
            "delivery",
            "late",
            "shipping",
            "parcel",
            "courier"
        ],
        "Service": [
            "staff",
            "support",
            "customer service",
            "employee",
            "behavior",
            "response"
        ]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "Other"


# -----------------------------------
# Priority Prediction
# -----------------------------------
def predict_priority(sentiment, category):

    if sentiment == "Negative":
        return "High"
    elif category == "Technical":
        return "Medium"
    else:
        return "Low"


# -----------------------------------
# Main AI Analyzer
# -----------------------------------
def analyze_complaint(text):
    sentiment = analyze_sentiment(text)
    category = detect_category(text)
    priority = predict_priority(sentiment, category)

    summary = text[:100]

    if sentiment == "Negative":
        suggestion = "This complaint should be resolved immediately by the support team."
    elif sentiment == "Neutral":
        suggestion = "Review the complaint and contact the customer if required."
    else:
        suggestion = "Thank the customer for the positive feedback."

    return {
        "Complaint": text,
        "Sentiment": sentiment,
        "Category": category,
        "Priority": priority,
        "Summary": summary,
        "Suggestion": suggestion
    }


# -----------------------------------
# Testing
# -----------------------------------
if __name__ == "__main__":
    complaint = input("Enter Complaint: ")

    result = analyze_complaint(complaint)

    print("\n===== AI Complaint Analysis =====")
    print("Complaint :", result["Complaint"])
    print("Sentiment :", result["Sentiment"])
    print("Category  :", result["Category"])
    print("Priority  :", result["Priority"])
    print("Summary   :", result["Summary"])
    print("Suggestion:", result["Suggestion"])  