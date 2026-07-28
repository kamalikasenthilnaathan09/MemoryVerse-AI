import sqlite3
import os


# Database location
DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "memoryverse.db"
)


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()


    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    connection.commit()

    connection.close()


    print("MemoryVerse AI database created successfully!")


if __name__ == "__main__":

    create_database()