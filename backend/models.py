from backend.database import db


class Complaint(db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    complaint = db.Column(db.Text, nullable=False)

    # AI Analysis Results
    sentiment = db.Column(db.String(20))
    category = db.Column(db.String(100))
    priority = db.Column(db.String(20))

    # AI Generated Information
    summary = db.Column(db.Text)
    suggestion = db.Column(db.Text)

    status = db.Column(db.String(20), default="Pending")

    created_at = db.Column(db.DateTime, server_default=db.func.now())