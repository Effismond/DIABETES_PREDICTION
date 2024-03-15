import streamlit as st

import pickle

import numpy as np


F=open("diabetes_model.pkl", "rb")

LR=pickle.load(F)

pregnancies=st.number_input("number of pregnancies:", 0,20,1)

glucose=st.number_input("Glucose:",0,900,1)

bp=st.number_input("Blood Pressure:", 0,180,1)

skin_thickness=st.number_input("Skin thickness:", 0,80,1)

Insulin=st.number_input("Insulin:", 30,300,30)

bmi=st.number_input("BMI:", 10,90,10)

DBF=st.number_input("Diabetes pedigree Function:",0.0,8.0,0.2)

AGE=st.number_input("Age:",0,150,1 )

data=[np.array([pregnancies,glucose,bp,skin_thickness,Insulin,bmi,DBF,AGE])]


Prediction=LR.predict(data)


if st.button("Diabetes Prediction"):

    st.write(str(Prediction))
    if Prediction==0:
        st.write("Diabetes")
    else:
        st.write(" Non Diabetes")
