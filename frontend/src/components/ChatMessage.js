import React from 'react';

function ChatMessage({ message, isUser }) {
  return (
    <div className={`message ${isUser ? 'message-user' : 'message-assistant'}`}>
      {message}
    </div>
  );
}

export default ChatMessage;