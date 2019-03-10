import sqlite3
from social.db import DATABASE_PATH

def add(follower, following):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO follow(follower, following)
                 VALUES (?,?)
        """, (follower, following))
