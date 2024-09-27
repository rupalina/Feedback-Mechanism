import psycopg2
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

def insert_feedback(question, answer, feedback_type, user_id=None, feedback_comment=None, accuracy_score=None):
    
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    insert_query = '''
    INSERT INTO feedback (question, answer, feedback_type, user_id, feedback_comment, accuracy_score)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING id;
    '''

    
    cur.execute(insert_query, (question, answer, feedback_type, user_id, feedback_comment, accuracy_score))
    feedback_id = cur.fetchone()[0]

  
    conn.commit()
    cur.close()
    conn.close()

    print(f"Feedback inserted with ID: {feedback_id}")

if __name__ == '__main__':
   
    insert_feedback(
        question="What is AI?",
        answer="AI stands for Artificial Intelligence.",
        feedback_type="Like",
        user_id=1,
        feedback_comment="Helpful",
        accuracy_score=2  
    )
