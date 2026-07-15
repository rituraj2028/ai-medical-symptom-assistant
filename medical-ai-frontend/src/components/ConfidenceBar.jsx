import "./ConfidenceBar.css";

function ConfidenceBar({ confidence }) {
  return (
    <div className="confidence-container">
      <div className="confidence-header">
        <span>Confidence</span>
        <span>{confidence}%</span>
      </div>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${confidence}%` }}
        ></div>
      </div>
    </div>
  );
}

export default ConfidenceBar;