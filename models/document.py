from datetime import datetime

from extensions import db


class Document(db.Model):
    """
    Stores uploaded document metadata.
    The actual file is saved in the uploads/ folder.
    """

    __tablename__ = "documents"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    original_filename = db.Column(
        db.String(255),
        nullable=False
    )

    stored_filename = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    file_type = db.Column(
        db.String(20),
        nullable=False
    )

    upload_time = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    processing_status = db.Column(
        db.String(30),
        default="Uploaded",
        nullable=False
    )

    extracted_text = db.Column(
        db.Text,
        nullable=True
    )

    ai_category = db.Column(
        db.String(100),
        nullable=True
    )

    def __repr__(self):
        return f"<Document {self.original_filename}>"