import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('titanic_model.pkl')

# Set up the Streamlit app
st.title('Titanic Survival Prediction')

# Create input fields for user to enter passenger details
pclass = st.selectbox("Ticket Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 1, 80, 25)
fare = st.slider("Fare", 0, 500, 50)
embarked = st.selectbox("Embarked", ["S", "C", "Q"])
family_size = st.slider("Family Size", 0, 10, 0)

# encoding the categorical variable 'sex'
sex = 1 if sex == "male" else 0
embarked = {"S": 2, "C": 0, "Q": 1}[embarked]

# Create a button to make the prediction
if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, fare, embarked, family_size]])
    result = model.predict(input_data)
    
    # Display the prediction result
    if result[0] == 1:
        st.success("✅ Survived!")
    else:
        st.error("❌ Not Survived")

