import { useEffect, useState } from "react";
import "./App.css";
import DocumentUpload from "./components/DocumentUpload";
import RagQuestionAnswer from "./components/RagQuestionAnswer";
import SemanticSearch from "./components/SemanticSearch";

function App() {
  const [backendStatus, setBackendStatus] = useState('Checking...')

useEffect(() => {
    const checkBackendHealth = async () => {
      try {
        const response = await fetch(
          `${import.meta.env.VITE_API_BASE_URL}/api/health`
        );

        if (!response.ok) {
          throw new Error("Backend health check failed");
        }

        const data = await response.json();
        setBackendStatus(data.message);
      } catch (error) {
        console.error(error);
        setBackendStatus("Backend is unavailable");
      }
    };

    checkBackendHealth();
  }, []);
 return (
    <main className="app-container">
      <header>
        <h1>DocuMind AI</h1>
        <p>Intelligent Document Q&A Platform</p>
        <p className="backend-status">
          Backend status: {backendStatus}
        </p>
      </header>

      <DocumentUpload />
      <RagQuestionAnswer />
      <SemanticSearch/>
    </main>
  );
}

export default App
