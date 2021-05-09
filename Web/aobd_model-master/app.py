import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

with (open('reg_model.pkl', 'rb')) as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)
    return render_template('index.html',prediction_text = 'Yield is {}'.format(output))
        
# @app.route('/predict_api',methods=['POST'])
# def results():
 
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=False)

