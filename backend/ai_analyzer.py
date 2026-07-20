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
        ],
        "Schools & Colleges": [
            "school",
            "college",
            "teacher",
            "principal",
            "class",
            "admission",
            "campus"
        ],
        "Security": [
            "security",
            "guard",
            "safety",
            "theft",
            "cctv",
            "attack",
            "police"
        ],
        "Canteen": [
            "canteen",
            "food",
            "mess",
            "cafeteria",
            "meal",
            "snack",
            "hygiene"
        ],
        "Maintenance": [
            "maintenance",
            "repair",
            "broken",
            "leak",
            "plumbing",
            "electric",
            "cleaning"
        ],
        "Company": [
            "company",
            "office",
            "manager",
            "employee",
            "workplace",
            "hr",
            "corporate",
            "policy"
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
def analyze_complaint(text, user_category=None):
    sentiment = analyze_sentiment(text)
    if user_category and user_category != "Select Category":
        category = user_category
    else:
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