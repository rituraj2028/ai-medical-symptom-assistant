import { useState } from "react";
import "./Home.css";
import SymptomSearch from "../components/SymptomSearch";
import api from "../services/api"
import PredictionCard from "../components/PredictionCard";
import DiseaseInfo from "../components/DiseaseInfo";
import AIExplanation from "../components/AIExplanation";
import SpecialistCard from "../components/SpecialistCard";
import TopPredictions from "../components/TopPredictions";
import AIChat from "../components/AIChat.jsx";

function Home() {

  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [prediction,setPrediction] = useState(null);
  const [loading,setLoading] = useState(false);


  const handlePredict = async () => {
    if(selectedSymptoms.length == 0){
        alert("Please select atleast one Symptom.");
        return;
    }
    try {
        setLoading(true);
        const response = await api.post("predict",{
            symptoms:selectedSymptoms
        });
        setPrediction(response.data)
    }
    catch(error){
        console.error(error);
        alert("Prediction Failed");
    }
    finally{
        setLoading(false);
    }


  }

  return (
    <div className="home">

      <h1>AI Medical Symptom Assistant</h1>

      <p>
        Predict possible diseases from symptoms using
        Deep Learning and Artificial Intelligence.
      </p>

      <SymptomSearch
        selectedSymptoms={selectedSymptoms}
        setSelectedSymptoms={setSelectedSymptoms}
      />

      <button 
      className = "predict-btn"
      onClick={handlePredict}
      >
        {loading ? "Predicting.." : "Predict Disease"}
      </button>

      {prediction && (
        <>
        <PredictionCard
        prediction = {prediction.prediction}
        />
        <DiseaseInfo
        prediction = {prediction.disease_information}
        />
        <AIExplanation
        explanation={prediction.ai_explanation}
        />
        <SpecialistCard
        specialist={prediction.disease_information.recommended_specialist}
        />
        <TopPredictions
        predictions={prediction.top_predictions}
        />
        <AIChat
        disease={prediction.prediction.disease}
        />
        </>
      )}
    </div>
  );
}

export default Home;