## import libraries
import streamlit as st
import keras 
from PIL import Image
import numpy as np

##load ann model
model = keras.models.load_model('heart_disease.h5')

# create function for prediction
def heart_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
    prediction = model.predict(input_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return 'You are likely to die from heart failure given your health condition'
    else:
        return 'You are not likely to die from heart failure given your health condition'

 ## page configuration   
def main():
    st.set_page_config(page_title='Heart Failure Predictor', layout='wide')

    ##
    image = Image.open('heart.png')
    st.image(image, use_column_width=False)

    ##set title and content
    st.title('Heart Failure Predictor using Artifical Neural Network')
    st.write('Enter your personal data to get health risk evaluation')

    ## get input from user
    age = st.number_input('Age of the patient:', min_value=0, step=1)
    anaemia = st.number_input('Anaemia | Yes or No | yes = 1 and no = 0:', min_value=0, step=1)
    creatinine_phosphokinase = st.number_input('Level of CPK enzyme in blood:', min_value=0, step=1)
    diabetes = st.number_input('Diabetes | Yes or No | yes = 1 and no = 0:', min_value=0, step=1)
    ejection_fraction = st.number_input('Percentage of blood leaving the heart:', min_value=0, step=1)
    high_blood_pressure = st.number_input('Hypertensive | Yes or No | yes = 1 and no = 0:', min_value=0, step=1)
    platelets = st.number_input('Platelet count of blood, (kiloplatelets/ml):', min_value=0, step=1)
    serum_creatinine = st.number_input('Level of serum creatinine in blood (mg/dl)', min_value=0, step=1)
    serum_sodium = st.number_input('Level of serum sodium in blood (mEq/L):', min_value=0, step=1)
    sex = st.number_input('Male or Female | Female = 1 and Male = 0:', min_value=0, step=1)
    smoking = st.number_input('Smoking | Yes or No | yes = 1 and no = 0:', min_value=0, step=1)
    time = st.number_input('Follow up period (days):', min_value=0, step=1)

    predict = ''

    if st.button('Predict'):
        predict = heart_prediction([age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium,	sex, smoking, time])
    st.success(predict)

if __name__ == '__main__':
    main()

## run using python -m streamlit run streamlit.py

