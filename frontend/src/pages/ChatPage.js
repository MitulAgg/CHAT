import React, { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import ChatMessage from '../components/ChatMessage';
import InputForm from '../components/InputForm';

import './ChatPage.css'; // Assuming you have a CSS file for styling

function ChatPage() {
  const { sessionId } = useParams();
  const [messages, setMessages] = useState([
    { text: "Hi there! How can I help you today?", isUser: false }
  ]);
  const chatContainerRef = useRef(null);

  const scrollToBottom = () => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleMessageSubmit = async (message) => {
    setMessages([...messages, { text: message, isUser: true }]);

    try {
      const response = await fetch('http://localhost:8000/chat/continue', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, session_id: sessionId }),
      });
      const data = await response.json();
      setMessages((prev) => [
        ...prev,
        { text: data.response, isUser: false },
      ]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="chat-page">
      <header className="chat-header">
        <h1>ChatBot</h1>
      </header>
      <div className="chat-container" ref={chatContainerRef}>
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg.text} isUser={msg.isUser} />
        ))}
      </div>
      <div className="chat-input-container">
        <InputForm
          onSubmit={handleMessageSubmit}
          placeholder="Ask me anything"
          buttonText="Send"
        />
      </div>
    </div>
  );
}

export default ChatPage;