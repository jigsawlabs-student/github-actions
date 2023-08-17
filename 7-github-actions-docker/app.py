import os
import numpy as np
from flask import Flask, request, jsonify
import joblib
import pdb
app = Flask(__name__)


def train_model():
    if not os.path.isfile('iris-model.model'):
        print('hello')
        train_model()


def load_model():
    model = joblib.load('iris-model.model')
    return model

@app.route('/predict', methods=['POST'])
def get_prediction():
    data = request.get_json()  # Get data posted as a json
    reshaped_data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
    prediction = model.predict_proba(reshaped_data)
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    model = load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80, debug = True)
