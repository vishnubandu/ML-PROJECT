import numpy as np
import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from flask import *

with open('model.pkl' ,'rb') as f:
   model=pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    sc = pickle.load(f)
app=Flask(__name__)
@app.route('/')
def base():
    return render_template('base.html')
@app.route('/predict')
def predict():
    return render_template('index.html')




@app.route('/submit',methods=["POST"])
def submit():
    CreditScore=int(request.form["credit_score"])
    Geography=request.form["geography"]
    if(Geography=="France"):
        Geography=0
    elif(Geography=="Germany"):
        Geography=1
    else:
        Geography=2
    Gender=request.form["gender"]
    if(Gender=='female'):
       Gender=0
    else:
       Gender=1
    Age=int(request.form["age"])
    Tenure=int(request.form["tenure"])     
    Balance=float(request.form["balance"])
    NumberOfProducts=int(request.form["number_of_products"])
    HasCrCard=request.form["has_cr_card"]
    if(HasCrCard=='yes'):
       HasCrCard=1
    else:
       HasCrCard=0
    IsActiveMember=request.form["is_active_member"]
    if(IsActiveMember=='yes'):
        IsActiveMember=1
    else:
        IsActiveMember=0
    EstimatedSalary=float(request.form["estimated_salary"])
    t=[[CreditScore,Geography,Gender,Age,Tenure,Balance,NumberOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]]
    i= sc.transform(t)
     
    x=model.predict(i)
    if(x[0]==0):
        return render_template("predNo.html")
    else:
        return render_template("predYes.html")





if __name__=='__main__':
    app.run(debug=True)

