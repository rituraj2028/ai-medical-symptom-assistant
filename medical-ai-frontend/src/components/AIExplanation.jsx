import "./AIExplanation.css";

function AIExplanation({ explanation }) {
  return (
    <div className="ai-card">

      <h2>🤖 AI Explanation</h2>

      <div className="ai-text">
        {explanation}
      </div>

    </div>
  );
}

export default AIExplanation;