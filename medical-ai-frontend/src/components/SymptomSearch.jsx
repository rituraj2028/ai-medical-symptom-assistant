import { useState,useEffect } from "react";
import { FaSearch } from "react-icons/fa";
import "./SymptomSearch.css"
import api from "../services/api"

function SymptomSearch({selectedSymptoms,setSelectedSymptoms}) {
  const [search, setSearch] = useState("");
  

  const [symptoms,setSymptoms] = useState([]);

  useEffect(() => {
    loadSymptoms();
  },[]);

  const loadSymptoms = async () =>{
    try{
      const response = await api.get("/symptoms");
      setSymptoms(response.data.symptoms);
    } catch (error){
      console.error(error)
    }
  };


  const filteredSymptoms = symptoms.filter(
    (symptom) =>
      symptom.toLowerCase().includes(search.toLowerCase()) &&
      !selectedSymptoms.includes(symptom)
  );

  const addSymptom = (symptom) => {
    setSelectedSymptoms([...selectedSymptoms, symptom]);
    setSearch("");
  };

  const removeSymptom = (symptom) => {
    setSelectedSymptoms(
      selectedSymptoms.filter((s) => s !== symptom)
    );
  };

  return (
    <div className="search-container">

      <div className="search-box">

        <FaSearch />

        <input
          type="text"
          placeholder="Search Symptoms..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

      </div>

      {search && (
        <div className="dropdown">
          {filteredSymptoms.map((symptom) => (
            <div
              key={symptom}
              className="dropdown-item"
              onClick={() => addSymptom(symptom)}
            >
              {symptom}
            </div>
          ))}
        </div>
      )}

      <div className="selected-container">
        {selectedSymptoms.map((symptom) => (
          <span
            key={symptom}
            className="chip"
            onClick={() => removeSymptom(symptom)}
          >
            {symptom} ✕
          </span>
        ))}
      </div>

    </div>
  );
}

export default SymptomSearch;