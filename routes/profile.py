from flask import Blueprint, render_template

from models.document import Document


dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard.route("/")
def home():

    documents = (
        Document.query
        .order_by(Document.upload_time.desc())
        .all()
    )

    return render_template(
        "dashboard.html",
        documents=documents
    )