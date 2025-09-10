# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:54:32 2023

@author: Dell
"""
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('2019_973.pkl','rb'))
model1 = pickle.load(open('cl19.pkl','rb'))
@app.route('/')
def home() : 
    return render_template("2019.html")
@app.route('/login',methods =['POST'])
def predict():
        if request.method == 'POST':

            selected_value = request.form['Age']
            mapped_value={'40-49':'0','50-59':'1','60 or older':'2','less than 40':'3'}.get(selected_value)
            Age = mapped_value or request.form['input_field']
            
            selected_value1 = request.form['Gender']
            mapped_value1={'Female':'0','Male':'1'}.get(selected_value1)
            Gender =mapped_value1 or request.form['input_field']

            selected_value2 = request.form['FD']
            mapped_value2={'No':'0','Yes':'1'}.get(selected_value2)
            FD =mapped_value2 or request.form['input_field']
            
            selected_value3 = request.form['BP']
            mapped_value3={'No':'0','Yes':'1'}.get(selected_value3)
            BP =mapped_value3 or request.form['input_field']
            
            selected_value4 = request.form['PA']
            mapped_value4={'less than half an hr':'0','more than half an hr':'1','Not Active':'2','one hr or more':'3'}.get(selected_value4)
            PA =mapped_value4 or request.form['input_field']
            
            selected_value5 = request.form['Smoking']
            mapped_value5={'No':'0','Yes':'1'}.get(selected_value5)
            Smoking =mapped_value5 or request.form['input_field']
            
            selected_value6 = request.form['Alcohol']
            mapped_value6={'No':'0','Yes':'1'}.get(selected_value6)
            Alcohol =mapped_value6 or request.form['input_field']

            selected_value7 = request.form['JF']
            mapped_value7={'Always':'0','Occasionally':'1','Often':'2','Very Often':'3'}.get(selected_value7)
            JF =mapped_value7 or request.form['input_field']
            
            selected_value8 = request.form['Stress']
            mapped_value8={'Always':'0','Not at all':'1','Sometimes':'2','Very Often':'3'}.get(selected_value8)
            Stress =mapped_value8 or request.form['input_field']
            
            selected_value9 = request.form['UF']
            mapped_value9={'Not Much':'0','Quite Often':'1'}.get(selected_value9)
            UF =mapped_value9 or request.form['input_field']
            
            BMI=request.form["BMI"].strip()
            Sleep=request.form["Sleep"].strip()
            Sound_Sleep=request.form["Sound_Sleep"].strip()
            Pregnancies=request.form["Pregnancies"].strip()            

            if Age == '' or Gender == '' or FD == '' or BP == '' or PA == '' or Smoking == '' or Alcohol == '' or JF == '' or Stress == '' or UF == '' or BMI == '' or Sleep == '' or Sound_Sleep == '' or Pregnancies == '':
                return render_template("2019.html", showcase="Please fill in all input fields.")
            else:
                input_data=[[int(Age),int(Gender),int(FD),int(BP),int(PA),int(Smoking),int(Alcohol),int(JF),int(Stress),int(UF),int(BMI),int(Sleep),int(Sound_Sleep),int(Pregnancies)]]

            y_pred = model.predict(input_data)[0]
            if y_pred == 1:
                output = "Diabetes"
                y_pred1 = model1.predict(input_data)[0]
                if y_pred1 == 0:
                    severity = 'Low'
                elif y_pred1 == 1:
                    severity = 'Medium'
                else:
                    severity = 'High'
            else:
                output = "No Diabetes"
                severity = 'You are healthy'
            return render_template('result.html', output=output,severity=severity)
            #return "Selected value: {}".format(selected_value)
if __name__ == '__main__':
        app.run(debug=True)