import numpy as np
import pickle
from flask import Flask, request ,render_template, jsonify


def load_model():
    file_name = "models/model.pkl"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
    

#model = pickle.load(open('model_pickle.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    #data = [float(x) for x in request.form.values()]
    #final_input = [np.array(data)]
    #print(final_input)

    request_json = request.get_json()
    final_input = [np.array(list(request_json.values()))]
    print(final_input)

    model = load_model()
    pred = model.predict(final_input)[0]

    #response = jsonify({'prediction': str(pred)})
    #response.headers.add('Access-Control-Allow-Origin', '*')

    return render_template("index.html",prediction_text="The predicted salary is {}".format(pred))

# Make a request
import requests

@app.route('/predict_api',methods=['POST'])
def predict_api():
    model = load_model()
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run(port=5000,debug=True)