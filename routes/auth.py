from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

auth = Blueprint("auth", __name__)


# ==========================
# Login
# ==========================
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        user = User.get_user_by_email(email)

        if user and check_password_hash(user[3], password):

            session["user"] = user[1]

            return redirect(url_for("auth.dashboard"))

        return render_template(
            "login.html",
            error="Invalid email or password"
        )

    return render_template("login.html")


# ==========================
# Register
# ==========================
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        hashed_password = generate_password_hash(password)

        try:

            User.create_user(
                name,
                email,
                hashed_password
            )

            return redirect(url_for("auth.login"))

        except Exception:

            return render_template(
                "register.html",
                error="Email already exists"
            )

    return render_template("register.html")


# ==========================
# Dashboard
# ==========================
@auth.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")


# ==========================
# Logout
# ==========================
@auth.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("home"))