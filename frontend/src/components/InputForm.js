import React, { useState, useRef, useEffect } from 'react';
import { FaArrowUp } from 'react-icons/fa';
import './InputForm.css'; // Assuming you have a CSS file for styling

function InputForm({ onSubmit, placeholder }) {
  const [input, setInput] = useState('');
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      onSubmit(input);
      setInput('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = Math.min(textarea.scrollHeight, 160) + 'px';
    }
  }, [input]);

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <div className="input-wrapper">
        <textarea
          ref={textareaRef}
          value={input}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          className="form-input"
          rows={1}
        />
        <button type="submit" className="arrow-button">
          <FaArrowUp />
        </button>
      </div>
    </form>
  );
}

export default InputForm;
