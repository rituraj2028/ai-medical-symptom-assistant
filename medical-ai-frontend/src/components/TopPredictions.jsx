import "./TopPredictions.css";

function TopPredictions({ predictions }) {

    return (

        <div className="top-predictions">

            <h2>🏆 Top Predictions</h2>

            {predictions.map((item, index) => (

                <div key={index} className="prediction-row">

                    <div>

                        <strong>
                            {index + 1}. {item.disease}
                        </strong>

                    </div>

                    <div>

                        {item.confidence}%

                    </div>

                    <div className="small-bar">

                        <div
                            className="small-fill"
                            style={{
                                width: `${item.confidence}%`
                            }}
                        ></div>

                    </div>

                </div>

            ))}

        </div>

    );

}

export default TopPredictions;