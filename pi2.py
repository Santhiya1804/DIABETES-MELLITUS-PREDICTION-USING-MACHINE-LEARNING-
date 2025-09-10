# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:10:47 2023
//Final Code Dec,KNN,SVC
@author: Dell
"""
#import numpy as np 
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('db76.pkl','rb'))
model1 = pickle.load(open('cl5.pkl','rb'))
@app.route('/')
def home() : 
    return render_template("cropyield.html")
@app.route('/login',methods =['POST'])
def predict():  
        age=request.form["age"].strip()
        p=request.form["p"].strip()
        gluc=request.form["gluc"].strip()
        BP=request.form["BP"].strip()
        bmi=request.form["bmi"].strip()
        St=request.form["St"].strip()
        pf=request.form["pf"].strip()
        ins=request.form["ins"].strip()
        if age == '' or p == '' or gluc == '' or BP == '' or bmi == '' or St == '' or pf == '' or ins == '':
            return render_template("cropyield.html", showcase="Please fill in all input fields.")
        else:
            input_data=[[int(age),int(p),int(gluc),int(BP),float(bmi),int(St),float(pf),int(ins)]]
    # Make a prediction using the diabetes model
        y_pred = model.predict(input_data)[0]
        if y_pred == 1:
            output = "Diabetes" 
            y_pred1 = model1.predict(input_data)[0]
            if y_pred1 == 0:
                severity = ' Patient diabetes is classified as Low'
            elif y_pred1 == 1:
                severity = ' Patient diabetes is classified as Medium'
            else:
                severity = ' Patient diabetes is classified as High'
        else:
            output="No diabetes"
            severity='You are healthy'
        return render_template("result.html", output=output,severity=severity)
       # return render_template("result1.html", severity=severity)
if __name__ == '__main__':
        app.run(debug=True)


