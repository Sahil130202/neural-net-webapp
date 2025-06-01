# Neural Network Web App (Iris Classifier)

This project is a simple custom-built neural network (from scratch using NumPy) trained on the Iris dataset. It comes with a lightweight Flask backend API and a clean HTML/CSS/JS frontend for making predictions interactively.

---

## 🚀 Features

- Neural Network implemented without any ML libraries (only NumPy)
- Trained on Iris dataset (3 classes)
- Web app with:
  - HTML form to input flower features
  - JavaScript frontend to fetch predictions
  - Flask API backend serving predictions
- Clean UI styled with CSS
- Easily deployable to AWS or any cloud platform

---

## 🖥️ Local Setup Instructions

### 📁 Folder Structure
```
neural-net-webapp/
├── backend/
│   ├── app.py               ← Flask API with neural network
│   └── model_weights.npy    ← (Optional) Saved weights
├── frontend/
│   ├── index.html           ← Input form + JS
│   ├── styles.css           ← CSS for layout
│   └── script.js            ← JS for API call
└── requirements.txt         ← Flask + dependencies
```

---

### 1. Clone the Repository
```bash
git clone https://github.com/Sahil130202/neural-net-webapp.git
cd neural-net-webapp
```

---

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
```

---

### 3. Frontend Setup
Open `frontend/index.html` in your browser  
OR  
Use **Live Server** in VS Code.

---

### 4. Test the App
- Fill in Sepal & Petal measurements
- Click Predict
- See the predicted Iris class below

---

## 🧠 How the Neural Network Works

- Input: 4 features (sepal length, sepal width, petal length, petal width)
- Hidden Layer: 8 neurons with ReLU
- Output Layer: 3 neurons with Softmax
- Trained using gradient descent and cross-entropy loss

---

## 📦 Tech Stack

- Python + Flask
- NumPy
- HTML + CSS + JavaScript (vanilla)
- CORS (for frontend/backend communication)

---

## 🌐 Deployment (Coming Soon)

Planned options:
- AWS EC2 (Python + Flask)
- GitHub Pages for frontend + AWS Lambda for backend
- Docker container setup for production

---

## 🐛 Common Errors & Fixes

- **CORS Error**: Make sure `flask-cors` is installed and `CORS(app)` is used
- **404/Network Error**: Confirm Flask is running and URL in `script.js` is `http://127.0.0.1:5000/predict`

---

## 📄 License

MIT License – free to use and modify.

---

## 📸 Screenshot (Optional)
Include a screenshot by placing an image in root and naming it `screenshot.png`.

```
![App Screenshot](screenshot.png)
```

