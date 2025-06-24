
// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
// import { FaPlus } from 'react-icons/fa';
// import InputForm from '../components/InputForm';

// function ContextPage() {
//   const navigate = useNavigate();
//   const [url, setUrl] = useState('');
//   const [showUrlInput, setShowUrlInput] = useState(false);

//   const handleContextSubmit = async (context) => {
//     try {
//       const payload = {
//         q: context,
//         url: showUrlInput && url.trim() !== '' ? url.trim() : null,
//       };

//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(payload),
//       });

//       const data = await response.json();
//       navigate(`/chat/${data.session_id}`);
//     } catch (error) {
//       console.error('Error creating session:', error);
//     }
//   };

//   return (
//     <div className="context-container">
//       <div className="context-card">
//         <h1 className="context-title">Welcome to ChatBot</h1>
//         <p className="context-description">
//           Enter your preferences or context to start a new chat session
//         </p>

//         <div className="input-with-url">
//           <InputForm
//             onSubmit={handleContextSubmit}
//             placeholder="Enter your preferences (e.g., 'Answer in a friendly tone')"
//             buttonText="Start Chat"
//           />
//           <button
//             type="button"
//             className="url-toggle-button"
//             onClick={() => setShowUrlInput(!showUrlInput)}
//             title={showUrlInput ? 'Remove URL' : 'Add URL'}
//           >
//             <FaPlus />
//           </button>
//         </div>

//         {showUrlInput && (
//           <div className="url-input-container">
//             <input
//               type="text"
//               className="url-input"
//               placeholder="Enter optional URL"
//               value={url}
//               onChange={(e) => setUrl(e.target.value)}
//             />
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }

// export default ContextPage;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaPlus, FaMinus } from 'react-icons/fa';
import InputForm from '../components/InputForm';
import './ContextPage.css'; // Assuming you have a CSS file for styling

function ContextPage() {
  const navigate = useNavigate();
  const [url, setUrl] = useState('');
  const [showUrlInput, setShowUrlInput] = useState(false);

  const handleContextSubmit = async (context) => {
    try {
      const payload = {
        q: context,
        url: showUrlInput && url.trim() !== '' ? url.trim() : null,
      };
      const response = await fetch(`http://localhost:8000/chat/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
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

        <div className="input-with-url">
          <InputForm
            onSubmit={handleContextSubmit}
            placeholder="Enter your preferences (e.g., 'Answer in a friendly tone')"
            buttonText="Start Chat"
          />

          <button
            type="button"
            className="url-toggle-button"
            onClick={() => setShowUrlInput(!showUrlInput)}
            aria-label={showUrlInput ? 'Remove URL' : 'Add URL'}
          >
            {showUrlInput ? <FaMinus /> : <FaPlus />}
          </button>
        </div>

        {showUrlInput && (
          <div className="url-input-container">
            <input
              type="text"
              className="url-input"
              placeholder="Enter optional URL"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default ContextPage;
