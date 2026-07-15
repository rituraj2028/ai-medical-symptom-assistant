import "./DiseaseInfo.css";

function DiseaseInfo({ prediction }) {
  return (
    <div className="disease-info">

      <h2>📖 Disease Information</h2>

      <h3>Description</h3>
      <p>{prediction.description}</p>

      <h3>Possible Causes</h3>
      <ul>
        {prediction.possible_causes?.map((cause, index) => (
          <li key={index}>{cause}</li>
        ))}
      </ul>

      <h3>Precautions</h3>
      <ul>
        {prediction.precautions?.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default DiseaseInfo;