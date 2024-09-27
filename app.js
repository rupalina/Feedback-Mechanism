function submitFeedback(feedbackType) {
    const data = {
        question: '{{question}}',
        answer: '{{answer}}',
        feedback_type: feedbackType,
        user_id: '{{user_id}}',  
        session_id: '{{session_id}}',  
        response_time: '{{response_time}}',  
        timestamp: new Date().toISOString()
    };

    fetch('/submit-feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Feedback submitted:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim()) {
        appendMessage('user', userInput);
        document.getElementById('user-input').value = '';
        fetchResponse(userInput);
    }
});

function appendMessage(sender, message) {
    const chatWindow = document.getElementById('chat-window');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(sender);
    messageDiv.innerText = message;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight; 
}

function fetchResponse(userInput) {
    
    setTimeout(() => {
        const botResponse = "This is a response from LISA"; 
        appendMessage('lisa', botResponse);
        
        appendFeedbackButtons();
    }, 1000);
}

function appendFeedbackButtons() {
    const chatWindow = document.getElementById('chat-window');
    const feedbackDiv = document.createElement('div');
    feedbackDiv.innerHTML = `
        <button class="like-btn" onclick="submitFeedback('like')">👍 Like</button>
        <button class="dislike-btn" onclick="submitFeedback('dislike')">👎 Dislike</button>
    `;
    chatWindow.appendChild(feedbackDiv);
}

function submitFeedback(feedbackType) {

    console.log('Feedback submitted:', feedbackType);
}
