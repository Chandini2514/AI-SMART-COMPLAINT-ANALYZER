from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Complaint
from backend.ai_analyzer import analyze_complaint

routes = Blueprint("routes", __name__)

@routes.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    data = request.get_json() or {}
    complaint_text = data.get("complaint", "")
    analysis = analyze_complaint(complaint_text, data.get("category"))

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

@routes.route("/complaints/<int:complaint_id>", methods=["DELETE"])
def delete_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if not complaint:
        return jsonify({
            "status": "Error",
            "message": "Complaint not found.",
        }), 404

    db.session.delete(complaint)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Complaint deleted successfully.",
    })

@routes.route("/complaints", methods=["GET"])
def get_complaints():
    complaints = Complaint.query.order_by(Complaint.created_at.desc()).all()
    return jsonify({
        "status": "Success",
        "data": [
            {
                "id": complaint.id,
                "name": complaint.name,
                "email": complaint.email,
                "complaint": complaint.complaint,
                "category": complaint.category,
                "priority": complaint.priority,
                "status": complaint.status,
                "summary": complaint.summary,
                "suggestion": complaint.suggestion,
                "created_at": complaint.created_at.strftime("%d-%m-%Y %H:%M"),
            }
            for complaint in complaints
        ]
    })
    