import React from 'react';
import { useNavigate } from 'react-router-dom';
import InputForm from '../components/InputForm';

function ContextPage() {
  const navigate = useNavigate();

  const handleContextSubmit = async (context) => {
    try {
      console.log("here");
      console.log(context);
      const response = await fetch(`http://localhost:8000/chat/?q=${encodeURIComponent(context)}`);
      const data = await response.json();
      navigate(`/chat/${data.session_id}`);
    } catch (error) {
      console.error('Error creating session:', error);
    }
  };

  return (
    <div className="context-container">
      <div className="context-card">
        <h1 className="context-title">Welcome to ChatBot</h1>
        <p className="context-description">
          Enter your preferences or context to start a new chat session
        </p>
        <InputForm
          onSubmit={handleContextSubmit}
          placeholder="Enter your preferences (e.g., 'Answer in a friendly tone')"
          buttonText="Start Chat"
        />
      </div>
    </div>
  );
}

export default ContextPage;