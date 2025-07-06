# db.py
import psycopg2
from psycopg2.extras import execute_values

# 🔐 Change these as needed
DB_CONFIG = {
    "host": "localhost",
    "database": "reviewlens",
    "user": "postgres",
    "password": "123456",
    "port": "5432"
}

def insert_review(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
            INSERT INTO review_insights
            (app_name, review, cleaned_review, label, confidence, urgency, keyphrases)
            VALUES %s;
        """
        values = [(data['app_name'], data['review'], data['cleaned_review'],
                   data['label'], data['confidence'], data['urgency'], data['keyphrases'])]

        execute_values(cursor, query, values)
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print("DB Insert Error:", e)
