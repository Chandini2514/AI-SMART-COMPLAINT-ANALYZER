from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Complaint
from backend.ai_analyzer import analyze_complaint

routes = Blueprint("routes", __name__)

@routes.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    data = request.get_json() or {}
    complaint_text = data.get("complaint", "")
    analysis = analyze_complaint(complaint_text)

    complaint = Complaint(
        name=data.get("name", ""),
        email=data.get("email", ""),
        complaint=complaint_text,
        sentiment=analysis["Sentiment"],
        category=analysis["Category"],
        priority=analysis["Priority"],
        summary=analysis["Summary"],
        suggestion=analysis["Suggestion"],
    )

    db.session.add(complaint)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Complaint submitted successfully!",
        "analysis": analysis,
    })
    