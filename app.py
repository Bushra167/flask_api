from flask import Flask,request,jsonify
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    x = request.form.get('x')
    y = request.form.get('y')
    z = request.form.get('z')

    input_query = np.array([[x, y, z]])

    result = model.predict(input_query)[0]

    return jsonify({'posture':result})

if __name__ == '__main__':
    app.run(debug=True)