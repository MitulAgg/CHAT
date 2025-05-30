import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ContextPage from './pages/ContextPage';
import ChatPage from './pages/ChatPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ContextPage />} />
        <Route path="/context" element={<ContextPage />} />
        <Route path="/chat/:sessionId" element={<ChatPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;