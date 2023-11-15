import pandas as pd
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
pipe=pickle.load(open("glucose_model.pkl",'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Age=request.form.get('Age')
    print(Age)
    input=pd.DataFrame([[Age]],columns=[Age])
    prediction=pipe.predict(input)[0]
    return str(prediction)


if __name__=="__main__":
    app.run(debug=True, port=5000)