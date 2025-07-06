import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(
        dbname="reviewlens",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

def fetch_reviews():
    conn = get_connection()
    query = "SELECT * FROM review_insights"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
