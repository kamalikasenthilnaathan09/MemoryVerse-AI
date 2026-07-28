import os
import uuid

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
)

from werkzeug.utils import secure_filename

from extensions import db
from models.document import Document


documents = Blueprint(
    "documents",
    __name__,
    url_prefix="/documents"
)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


@documents.route("/upload", methods=["GET", "POST"])
def upload_document():

    if request.method == "POST":

        if "document" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["document"]

        if file.filename == "":
            flash("Please choose a file.", "warning")
            return redirect(request.url)

        if file and allowed_file(file.filename):

            original_filename = secure_filename(file.filename)

            extension = original_filename.rsplit(".", 1)[1].lower()

            stored_filename = (
                f"{uuid.uuid4().hex}.{extension}"
            )

            upload_folder = current_app.config["UPLOAD_FOLDER"]

            os.makedirs(upload_folder, exist_ok=True)

            file.save(
                os.path.join(
                    upload_folder,
                    stored_filename
                )
            )

            document = Document(
                original_filename=original_filename,
                stored_filename=stored_filename,
                file_type=extension
            )

            db.session.add(document)
            db.session.commit()

            flash(
                "Document uploaded successfully!",
                "success"
            )

            return redirect(
                url_for("documents.upload_document")
            )

        flash(
            "Unsupported file type.",
            "danger"
        )

    return render_template("upload.html")