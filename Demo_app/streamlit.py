
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("Diabetes_Model.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Glucose,BMI,Age,DiabetesPedigreeFunction): 

    arr=np.array([[Glucose,BMI,Age,DiabetesPedigreeFunction]])    
    prediction=classifier.predict(arr)
    print(prediction)
    return prediction



def main():
    #st.markdown('<div style="text-align: center;"><h1>Thyroid Prediction</h1></div>', unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:pink;padding:1px; margin-bottom:40px">
    <h1 style="color:black;text-align:center;">DIABETES PREDICTION ML APP </h1>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
        st.session_state.placeholder = "Type Here"

    Glucose = st.text_input(":red[Glucose] 👇",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder=st.session_state.placeholder,)
    BMI = st.text_input(":red[BMI] 👇",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder=st.session_state.placeholder,)
    Age = st.text_input(":red[Age] 👇",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder=st.session_state.placeholder,)
    DiabetesPedigreeFunction = st.text_input(":red[DiabetesPedigreeFunction]👇",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder=st.session_state.placeholder,)
    result=""
    
    col1, col2, col3 , col4, col5 = st.columns([1,1,1,1,1])

    with col1:
        pass
    with col1:
        pass
    with col3:
        button=st.button('Predict',type="primary")
    with col4:
        pass
    with col5:
        pass
    if button:
        result=predict_note_authentication(Glucose,BMI,Age,DiabetesPedigreeFunction)
        if result == 0:
            html_temp = """
            <div style="background-color:red;padding:1px">
            <h3 style="color:white;text-align:center;">SORRY You Have Diabetes </h3>
            </div>
            """
            st.markdown(html_temp,unsafe_allow_html=True)    
            # st.error("SORRY You are positive")
        else:
            html_temp = """
            <div style="background-color:green;padding:1px">
            <h3 style="color:white;text-align:center;">CONGRATULATION You Do Not Have Diabetes</h3>
            </div>
            """
            st.markdown(html_temp,unsafe_allow_html=True)
            # st.success("CONGRATULATION You are Negative")


if __name__=='__main__':
    main()
