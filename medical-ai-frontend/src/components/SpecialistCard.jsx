import "./SpecialistCard.css";

function SpecialistCard({ specialist }) {
    return (
        <div className="specialist-card">

            <h2>👨‍⚕️ Recommended Specialist</h2>

            <h3>{specialist}</h3>

            <p>
                Please consult this specialist for a proper diagnosis
                and treatment.
            </p>

        </div>
    );
}

export default SpecialistCard;