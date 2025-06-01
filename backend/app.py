from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

W1 = np.random.randn(4,8)
b1 = np.zeros((1,8))
W2 = np.random.randn(8,3)
b2 = np.zeros((1,3))

def relu(z):
    return np.maximum(0,z)

def softmax(z):
    exp = np.exp(z-np.max(z,axis=1,keepdims=True))
    return exp / np.sum(exp, axis=1, keepdims=True)

def forward(X):
    z1 = np.dot(X, W1) +b1
    a1 = relu(z1)
    z2 = np.dot(a1, W2) + b2
    return softmax(z2)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data[features].reshape(1, -1))
    prediction = np.argmax(forward(features))
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)