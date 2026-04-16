import { useState } from "react";

function App() {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    const data = {
      GENDER: 1,
      AGE: 65,
      SMOKING: 1,
      YELLOW_FINGERS: 2,
      ANXIETY: 2,
      PEER_PRESSURE: 1,
      CHRONIC_DISEASE: 1,
      FATIGUE: 2,
      ALLERGY: 1,
      WHEEZING: 2,
      ALCOHOL_CONSUMING: 2,
      COUGHING: 2,
      SHORTNESS_OF_BREATH: 2,
      SWALLOWING_DIFFICULTY: 2,
      CHEST_PAIN: 2,
    };

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const json = await res.json();
    setResult(json);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Lung Cancer Risk Predictor</h1>

      <button onClick={handlePredict}>Predict Risk</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Result:</h3>
          <p><b>Label:</b> {result.label}</p>
          <p><b>Probability:</b> {result.probability}</p>

          <h4>Explanation:</h4>
          <ul style={{ listStyleType: "none", padding: 0 }}>
  {result.explanation.map((item, index) => (
    <li key={index} style={{ marginBottom: "8px" }}>• {item}</li>
  ))}
</ul>
        </div>
      )}
    </div>
  );
}

export default App;