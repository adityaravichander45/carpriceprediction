import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

st.title('Car price prediction')

def predict(data):
    model = joblib.load('model.pkl')
    return model.predict(data)

dat = pd.read_csv('carprice.csv')
dat

Name = st.text_input('Enter the name of the car')
st.write('The name of the car is', Name)

Year = st.selectbox(
   "What is the year of the car?",
   ('2018', '2020', '2012', '2019', '2017', '2016', '2015', '2014', '2010', '2013', '2011', '2021', '2022', '2009', '2023'),
   index=None,
   placeholder="Select the Year...",
)

st.write('You selected:', Year)


Miles = st.number_input("Enter the mileage", value=None, placeholder="Type the mileage...")

st.write('You selected:', Miles)


Price = st.number_input("Enter the price", value=None, placeholder="Type the price...")

st.write('You selected:', Price)

# creating a button click to call the predict method
result=""

if st.button("Predict"):
    result=predict_subscribe(Name,Year,Miles,Price)

#displaying the results
if result==1:
    st.success("potential car model")
elif result==0:
    st.success("Not a potential car model")


# program starter
if __name__ =='__main__':
	main()
