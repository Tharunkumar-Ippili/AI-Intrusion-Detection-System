import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🔐 AI-Based Intrusion Detection System")

st.write("Enter network traffic details:")

# Simple inputs (demo)
duration = st.number_input("Duration", 0)
src_bytes = st.number_input("Source Bytes", 0)
dst_bytes = st.number_input("Destination Bytes", 0)

protocol = st.selectbox("Protocol", ["tcp", "udp", "icmp"])
service = st.text_input("Service (e.g., http, ftp)")
flag = st.text_input("Flag (e.g., SF)")

if st.button("Check Traffic"):

    # Create input dataframe
    input_dict = {
        "duration": duration,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes
    }

    df = pd.DataFrame([input_dict])

    # Add missing columns
    for col in columns:
        if col not in df:
            df[col] = 0

    df = df[columns]

    # Predict
    prediction = model.predict(df)[0]

    if prediction == 0:
        st.success("✅ Normal Traffic")
    else:
        st.error("🚨 Attack Detected!")