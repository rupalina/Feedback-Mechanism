import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_all_feedback():
    
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    
    cur = conn.cursor()

    cur.execute("SELECT * FROM feedback;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    get_all_feedback()
