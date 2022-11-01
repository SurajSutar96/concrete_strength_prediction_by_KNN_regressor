
from flask import Flask,request,render_template,jsonify
import pickle
import json

with open('concrete_model.pkl','rb')as f:
    model=pickle.load(f)
with open('std_scalar.pkl','rb')as f:
    std_scalar=pickle.load(f)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=["POST"])
def predict():
    array=[float(x) for x in request.form.values()]
    array_new=std_scalar.transform([array])
    pred=model.predict(array_new)[0].round(2)
    return render_template("home.html",predictions=f"Strength of concrete is :- {pred} kn/sqm")
if __name__=="__main__":
    app.run(port=3434,debug=True)
