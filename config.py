import os

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration for MemoryVerse AI"""

    # ------------------------
    # Flask
    # ------------------------
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "memoryverse_ai_super_secret_key"
    )

    # ------------------------
    # Database
    # ------------------------
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.path.join(BASE_DIR, 'database', 'memoryverse.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ------------------------
    # File Uploads
    # ------------------------
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 20 MB

    ALLOWED_EXTENSIONS = {
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "docx"
    }

    # ------------------------
    # OCR
    # ------------------------
    OCR_LANGUAGE = "eng"

    # ------------------------
    # AI
    # ------------------------
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    DEFAULT_AI_PROVIDER = "local"

    # ------------------------
    # Timeline
    # ------------------------
    TIMELINE_ITEMS_PER_PAGE = 20

    # ------------------------
    # Search
    # ------------------------
    SEARCH_RESULTS_LIMIT = 10