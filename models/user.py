import sqlite3
import os


DATABASE_PATH = os.path.join(
    "database",
    "memoryverse.db"
)


class User:


    @staticmethod
    def create_user(name, email, password):

        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO users
            (name, email, password)

            VALUES (?, ?, ?)
            """,

            (name, email, password)

        )


        connection.commit()

        connection.close()



    @staticmethod
    def get_user_by_email(email):

        connection = sqlite3.connect(DATABASE_PATH)

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,

            (email,)

        )


        user = cursor.fetchone()


        connection.close()


        return user