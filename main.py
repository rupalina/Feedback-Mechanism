from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv
import re
import time
from datetime import datetime

load_dotenv()

app = Flask(__name__)
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = conn.cursor()

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def get_last_feedback_time(user_id):
    return None

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    feedback_data = request.json

    try:
        
        question = feedback_data.get('question')
        answer = feedback_data.get('answer')
        feedback_type = feedback_data.get('feedback_type')
        user_id = feedback_data.get('user_id')
        feedback_comment = feedback_data.get('feedback_comment')
        accuracy_score = feedback_data.get('accuracy_score')
        if accuracy_score is not None:
            try:
                accuracy_score = float(accuracy_score)
                if not (0 <= accuracy_score <= 5):
                    raise ValidationError("Accuracy score must be between 0 and 5")
            except ValueError:
                raise ValidationError("Accuracy score must be a number")

       
        if not question or not answer:
            raise ValidationError("Question and answer are required and cannot be empty")

        
        valid_feedback_types = ['Like', 'Dislike']
        if feedback_type not in valid_feedback_types:
            raise ValidationError("Feedback type must be one of the following: " + ", ".join(valid_feedback_types))

        if user_id is None:
            raise ValidationError("User ID cannot be empty.")

        if user_id is not None and not isinstance(user_id, int):
            raise ValidationError("User ID must be an integer.")

        
        if feedback_comment and (len(feedback_comment) < 10 or len(feedback_comment) > 500):
            raise ValidationError("Feedback comment must be between 10 and 500 characters")

        insert_query = """
        INSERT INTO feedback (question, answer, feedback_type, user_id, feedback_comment, accuracy_score)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(insert_query, (question, answer, feedback_type, user_id, feedback_comment, accuracy_score))
        conn.commit()

        return jsonify({"status": "success", "message": "Thank you for your feedback!"}), 200

    except ValidationError as e:
        return jsonify({"status": "error", "message": e.message}), 400  
        return jsonify({"status": "error", "message": str(e)}), 500  
if __name__ == '__main__':
    app.run(debug=False)
