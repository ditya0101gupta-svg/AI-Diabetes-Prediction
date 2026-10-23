import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

@st.cache_resource
def load_resources():
    model = joblib.load("models/random_forest_model.pkl")
    imputer = joblib.load("models/imputer.pkl")
    features = joblib.load("models/feature_names.pkl")
    return model, imputer, features

model, imputer, features = load_resources()

st.title("🩺 AI-Based Diabetes Prediction System")
st.write("Enter health information to generate a machine learning prediction.")

st.info(
    "Educational project only. This model cannot diagnose "
    "or rule out diabetes."
)

labels = {'HighBP': 'High Blood Pressure', 'HighChol': 'High Cholesterol', 'CholCheck': 'Cholesterol Checked in Past 5 Years', 'BMI': 'Body Mass Index (BMI)', 'Smoker': 'Smoked at Least 100 Cigarettes in Lifetime', 'Stroke': 'History of Stroke', 'HeartDiseaseorAttack': 'Heart Disease or Heart Attack', 'PhysActivity': 'Physical Activity in Past 30 Days', 'Fruits': 'Consumes Fruit Daily', 'Veggies': 'Consumes Vegetables Daily', 'HvyAlcoholConsump': 'Heavy Alcohol Consumption Indicator', 'AnyHealthcare': 'Has Healthcare Coverage', 'NoDocbcCost': 'Could Not See Doctor Due to Cost', 'GenHlth': 'General Health Rating', 'MentHlth': 'Poor Mental Health Days (Past 30 Days)', 'PhysHlth': 'Poor Physical Health Days (Past 30 Days)', 'DiffWalk': 'Difficulty Walking or Climbing Stairs', 'Sex': 'Sex', 'Age': 'Age Group', 'Education': 'Education Level', 'Income': 'Income Category'}

category_labels = {'Age': {1: '18–24', 2: '25–29', 3: '30–34', 4: '35–39', 5: '40–44', 6: '45–49', 7: '50–54', 8: '55–59', 9: '60–64', 10: '65–69', 11: '70–74', 12: '75–79', 13: '80 or older'}, 'GenHlth': {1: 'Excellent', 2: 'Very Good', 3: 'Good', 4: 'Fair', 5: 'Poor'}, 'Education': {1: 'Never Attended School', 2: 'Elementary School', 3: 'Some High School', 4: 'High School Graduate', 5: 'Some College', 6: 'College Graduate'}, 'Income': {1: 'Less than $10,000', 2: '$10,000–$14,999', 3: '$15,000–$19,999', 4: '$20,000–$24,999', 5: '$25,000–$34,999', 6: '$35,000–$49,999', 7: '$50,000–$74,999', 8: '$75,000 or more'}}

# Input fields
with st.form("prediction_form"):

    st.subheader("Patient Health Information")

    user_inputs = {}

    for feature in features:
        if feature == "BMI":
            user_inputs[feature] = st.number_input(
                "BMI",
                min_value=10.0,
                max_value=100.0,
                value=25.0
            )

        elif feature == "Age":
            user_inputs[feature] = st.selectbox(
                "Age Group",
                options=list(category_labels["Age"].keys()),
                index=6,
                format_func=lambda x: category_labels["Age"][x]
            )

        elif feature in ["GenHlth", "MentHlth", "PhysHlth",
                         "Education", "Income"]:
            limits = {
                "GenHlth": (1, 5),
                "MentHlth": (0, 30),
                "PhysHlth": (0, 30),
                "Education": (1, 6),
                "Income": (1, 8)
            }

            low, high = limits[feature]

            if feature in category_labels:
                user_inputs[feature] = st.selectbox(
                    labels.get(feature, feature),
                    options=list(category_labels[feature].keys()),
                    format_func=lambda x: category_labels[feature][x]
                )
            else:
                user_inputs[feature] = st.number_input(
                    labels.get(feature, feature),
                    min_value=low,
                    max_value=high,
                    value=low
                )

        elif feature == "Sex":
            user_inputs[feature] = st.selectbox(
                "Sex",
                options=[0, 1],
                format_func=lambda x: "Male" if x == 1 else "Female"
            )

        else:
            user_inputs[feature] = st.selectbox(
                labels.get(feature, feature),
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No"
            )

    submitted = st.form_submit_button(
        "Predict Diabetes Classification",
        use_container_width=True
    )

if submitted:

    input_df = pd.DataFrame([user_inputs])
    input_df = input_df[features]

    processed_input = imputer.transform(input_df)

    prediction = model.predict(processed_input)[0]
    probability = model.predict_proba(processed_input)[0][1]


    st.divider()
    st.subheader("Prediction Results Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Class",
            "Class 1" if prediction == 1 else "Class 0"
        )

    with col2:
        st.metric(
            "Estimated Class 1 Probability",
            f"{probability * 100:.2f}%"
        )

    st.subheader("Model Probability Visualization")

    st.progress(float(probability))

    st.caption(
        "The bar represents the model's estimated probability "
        "for class 1, not a clinically validated risk score."
    )

    if prediction == 1:
        st.warning(
            "The model classified this input as Diabetes (1). "
            "This is not a medical diagnosis."
        )
    else:
        st.info(
            "The model classified this input as Non-Diabetes (0). "
            "This does not rule out diabetes."
        )

    st.subheader("Important Information")

    st.write(
        "This prediction was generated using a Random Forest "
        "machine learning model trained on the BRFSS 2015 dataset."
    )

    st.write(
        "The dataset contains self-reported health indicators. "
        "The model is intended for educational demonstration "
        "and has not been clinically validated."
    )

    st.info(
        "For diabetes screening or diagnosis, consult a "
        "qualified healthcare professional."
    )
