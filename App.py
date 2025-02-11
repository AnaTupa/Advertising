import streamlit as st
import pickle
import pandas as pd

# Title
st.title('Sales Prediction App')

st.write('This web app predicts the **Sales** based on advertising factors.')

#to read the model from the pickle file
model=pickle.load(open('advertising_model.pkl','rb'))

# get input from the user  TV	Radio	Newspaper	Sales
inv_tv=st.number_input('TV Advertisement Budget ($) min: 0.7 max: 293.60')
inv_radio=st.number_input('Radio Advertisement Budget ($) min:0.00 max: 49.6')
inv_newspaper=st.number_input('Newspaper Advertisement Budget ($) min: 0.30 max: 89.4')

# convert the user information in DataFrame
user_data=pd.DataFrame({
    'TV':inv_tv,
    'Radio':inv_radio,
    'Newspaper':inv_newspaper}, index=[0])

# predict the house proce
prediction=model.predict(user_data)

if st.button('Predict'):
        st.write(f'Predict Sales in units: {prediction[0]*1000}')