
import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    pred=model.predict(final_features)
    return render_template('index.html',prediction_text='the custmer belongs to cluster {}'.format(pred))

if __name__ =="__main__":
    app.run(debug=True)
    

