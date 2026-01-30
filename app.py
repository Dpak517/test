import streamlit as st
import numpy as np
import pandas as pd
import pickle
import warnings

from streamlit.elements.bokeh_chart import BokehMixin

warnings.filterwarnings("ignore")


model=pickle.load(open('model.pkl','rb'))
print('Hi this is Diabetes predictor.')

#st.title(':rainbow[Diabetes Predictor] :sunglasses:')
#st.header('It will :green[detect] ')


def diabetes_prediction(user):
    model=pickle.load(open('model.pkl','rb'))
    user_input=np.asarray(user,dtype=float).reshape(1,-1)
    pred=model.predict(user_input)
    print(pred)
    if pred==0:
        return 'You are safe bro.'
    else:
        return 'You are done lit bro.'

def main():
    #giving title
    st.title(':rainbow[Diabetes Predictor Web ***App***] :sunglasses:')


   #getting input data
    Pregnancies=st.text_input('Total number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure level')
    SkinThickness=st.text_input('SkinThickness level')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree function value')
    Age=st.text_input('Age')

    #code
    diagnosis=''

    if st.button('Diabetes Result',type='primary',icon="⭐"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        st.balloons()


    st.success(diagnosis)
    st.toast('So whats ur decison',icon='😘',duration='short')


if __name__=='__main__':
    main()







