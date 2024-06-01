import streamlit as st
import pandas as pd
import joblib

# this is the main function in which we define our webpage  
def main():
    st.markdown("# Wine Quality Prediction App 🍷🍇 💋‍")
    st.markdown("### This app is meant to predict red wine quality " +
             "according to different chemical properties.")
    st.image('wine_image.jpg')  # Add an image

# Init code
if __name__=='__main__': 
    main()  

# Load the trained model
model = joblib.load('model.joblib')

# Create columns
col1, col2 = st.columns(2)

# input number version 
with col1:
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=15.0, value=7.4)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, value=0.7)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.3)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=20.0, value=2.0)

with col2:
    chlorides = st.slider('Chlorides', 0.0, 1.0, 0.05, 0.001)
    free_sulfur_dioxide = st.slider('Free Sulfur Dioxide', 0.0, 100.0, 15.0, 1.0)
    total_sulfur_dioxide = st.slider('Total Sulfur Dioxide', 0.0, 300.0, 46.0, 1.0)
    density = st.slider('Density', 0.9900, 1.0040, 0.9968, 0.0001)
    pH = st.slider('pH', 2.0, 4.0, 3.3, 0.01)
    sulphates = st.slider('Sulphates', 0.0, 2.0, 0.5, 0.01)
    alcohol = st.slider('Alcohol', 8.0, 15.0, 10.5, 0.1)

# Create a DataFrame to gather all these values, case sensitive
chemicals_df = pd.DataFrame({
    'fixed acidity': [fixed_acidity],
    'volatile acidity': [volatile_acidity],
    'citric acid': [citric_acid],
    'residual sugar': [residual_sugar],
    'chlorides': [chlorides],
    'free sulfur dioxide': [free_sulfur_dioxide],
    'total sulfur dioxide': [total_sulfur_dioxide],
    'density': [density],
    'pH': [pH],
    'sulphates': [sulphates],
    'alcohol': [alcohol]
})

# Display the values in the DataFrame
st.dataframe(chemicals_df)

# Create a button for prediction
if st.button('Predict Wine Quality'):
    # Use the model to predict the wine quality
    prediction = model.predict(chemicals_df)

    # Display the prediction
    st.write('The predicted wine quality is:', prediction[0])