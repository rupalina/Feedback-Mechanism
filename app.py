import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os


load_dotenv()


DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}


try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS feedback (
        id SERIAL PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        feedback_type VARCHAR(10) CHECK (feedback_type IN ('Like', 'Dislike')) NOT NULL,
        user_id INT NOT NULL,
        feedback_comment TEXT,
        accuracy_score FLOAT8
    );
    '''

    cur.execute(create_table_query)
    conn.commit()

    
    print("Feedback table created successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
 
    if cur:
        cur.close()
    if conn:
        conn.close()
