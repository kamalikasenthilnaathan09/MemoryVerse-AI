from flask import Flask, render_template

from config import Config
from extensions import db

from routes.auth import auth
from routes.documents import documents
from routes.dashboard import dashboard

app = Flask(__name__)

# ==========================
# Load Configuration
# ==========================

app.config.from_object(Config)

# ==========================
# Initialize Extensions
# ==========================

db.init_app(app)

# ==========================
# Register Blueprints
# ==========================

app.register_blueprint(auth)
app.register_blueprint(documents)
app.register_blueprint(dashboard)

# ==========================
# Home Route
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)