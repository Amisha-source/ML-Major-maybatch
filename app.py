# It is a magic command to create app.py file
import streamlit as st
import joblib
st.title('Reviews Deployment')
test_model = joblib.load('Reviews')
ip = st.text_input('Enter your Review')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])