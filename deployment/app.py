import streamlit as st
import pandas as pd
import pickle

st.title("🔐 Phishing Website Detection")

st.write("Upload a CSV file containing website feature values to check if the site is Legitimate or Phishing.")

# Load saved objects
model = pickle.load(open(r"deployment\final_model.pkl", "rb"))
preprocessor = pickle.load(open(r"deployment\preprocessor.pkl", "rb"))
pca = pickle.load(open(r"deployment\pca.pkl", "rb"))
features = pickle.load(open(r"deployment\features.pkl", "rb"))

uploaded_file = st.file_uploader("Upload test_input.csv file", type=["csv"])

if uploaded_file is not None:

    input_df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.dataframe(input_df)

    # Ensure correct column order
    input_df = input_df[features]
    # Apply preprocessing
    input_processed = preprocessor.transform(input_df)

    # Apply PCA
    input_pca = pca.transform(input_processed)

    # Prediction
    prediction = model.predict(input_pca)

    if prediction[0] == 1:
        st.error("⚠️ Phishing Website Detected")
    else:
        st.success("✅ Legitimate Website")

    # Preprocess
    data_preprocessed = preprocessor.transform(input_df)

    # Apply PCA
    data_pca = pca.transform(data_preprocessed)

    # Predict
    prediction = model.predict(data_pca)

    results = pd.DataFrame({
        "Prediction": prediction
    })

    results["Prediction"] = results["Prediction"].map({
        0: "Legitimate",
        1: "Phishing"
    })

    st.subheader("Prediction Result")
    st.dataframe(results)