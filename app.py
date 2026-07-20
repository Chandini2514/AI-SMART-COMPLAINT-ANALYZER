from backend import create_app
from backend.database import db

app = create_app()

# Home Route
@app.route("/")
def home():
    return {
        "status": "Success",
        "message": "AI Smart Complaint Analyzer Backend Running!"
    }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)