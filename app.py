import streamlit as st
import joblib
import numpy as np

# Page Config
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    border: none;
}

.prediction-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #1E1E1E;
    text-align: center;
    font-size: 24px;
    color: #00FFAA;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load('models/model.pkl')

# Title
st.title("💰 Insurance Premium Prediction")

st.write(
    "Predict insurance premium based on customer details."
)

# Input Fields
age = st.slider(
    "Age",
    18,
    100,
    25
)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.slider(
    "BMI",
    10.0,
    50.0,
    25.0
)

children = st.slider(
    "Children",
    0,
    10,
    0
)

smoker = st.selectbox(
    "Smoker",
    ["Yes", "No"]
)

region = st.selectbox(
    "Region",
    [
        "northwest",
        "northeast",
        "southwest",
        "southeast"
    ]
)

# Encoding
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

region_map = {
    "northwest":0,
    "northeast":1,
    "southwest":2,
    "southeast":3
}

region = region_map[region]

# Prediction
if st.button("Predict Premium"):

    input_data = np.array([
        [
            age,
            sex,
            bmi,
            children,
            smoker,
            region
        ]
    ])

    prediction = model.predict(input_data)

    st.markdown(
        f"""
        <div class="prediction-box">
            Predicted Premium <br><br>
            ₹ {prediction[0]:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )