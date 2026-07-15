import "./PredictionCard.css";
import ConfidenceBar from './ConfidenceBar';
import DiseaseInfo from "./DiseaseInfo";

function PredictionCard({ prediction }) {

    return (
        <div className="prediction-card">

            <h2>🩺 Predicted Disease</h2>

            <h1>{prediction.disease}</h1>
            <ConfidenceBar confidence= {prediction.confidence}  />

        </div>
    );

}

export default PredictionCard;