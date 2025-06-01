document.getElementById("predictForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const features = [
      parseFloat(document.getElementById("f1").value),
      parseFloat(document.getElementById("f2").value),
      parseFloat(document.getElementById("f3").value),
      parseFloat(document.getElementById("f4").value),
    ];
  
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features })
    });
  
    const result = await response.json();
    document.getElementById("result").innerText = `Predicted Class: ${result.prediction}`;
  });
  