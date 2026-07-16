import axios from "axios";

const api = axios.create({
    baseURL: "https://ai-medical-symptom-assistant.onrender.com",
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;