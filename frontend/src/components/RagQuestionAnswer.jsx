import { useState } from "react";

const RagQuestionAnswer = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [citations, setCitations] = useState([]);
  const [isAnswering, setIsAnswering] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async (event) => {
  event.preventDefault();

  const trimmedQuestion = question.trim();

  if (!trimmedQuestion) {
    return;
  }

  setError("");
  setAnswer("");
  setCitations([]);
  setIsAnswering(true);

  try {
    const response = await fetch(
      `${import.meta.env.VITE_API_BASE_URL}/api/rag/answer`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: trimmedQuestion,
          number_of_results: 4,
        }),
      }
    );

    const data = await response.json();

    if (!response.ok) {
      throw new Error(
        data.detail || "Failed to generate answer"
      );
    }

    setAnswer(data.answer);
    setCitations(data.citations ?? []);
  } catch (error) {
    setError(error.message);
  } finally {
    setIsAnswering(false);
  }
    };

  return (
    <section className="rag-card">
      <h2>Ask your documents</h2>

      <p>
        Get a grounded answer with source and page citations.
      </p>

      <form onSubmit={handleSubmit}>
        <textarea
          value={question}
          placeholder="Ask a question about your documents"
          disabled={isAnswering}
          onChange={handleChange}
          rows={4}
        />

        <button
          type="submit"
          disabled={
            question.trim() === "" || isAnswering
          }
        >
          {isAnswering ? "Generating..." : "Ask"}
        </button>
      </form>
      {error && (
  <p className="rag-error">
    {error}
  </p>
)}

{answer && (
  <div className="rag-answer">
    <h3>Answer</h3>
    <p>{answer}</p>
  </div>
)}

{citations.length > 0 && (
  <div className="rag-citations">
    <h3>Sources</h3>

    {citations.map((citation) => (
      <details
        className="citation-card"
        key={citation.citation_id}
      >
        <summary>
          [{citation.citation_id}]{" "}
          {citation.source}

          {citation.page_number != null && (
            <>
              {" "}· Page: {citation.page_number}
            </>
          )}

          {" "}· Chunk: {citation.chunk_index}
        </summary>

        <p>{citation.content}</p>

        <small>
          Vector distance:{" "}
          {citation.distance.toFixed(3)}
        </small>
      </details>
    ))}
  </div>
)}
    </section>
  );
};

export default RagQuestionAnswer;