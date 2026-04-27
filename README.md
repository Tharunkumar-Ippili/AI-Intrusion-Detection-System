# 🔐 AI-Based Intrusion Detection System (IDS)

## 📌 Overview
This project presents a Machine Learning-based Intrusion Detection System (IDS) designed to identify malicious network traffic and potential cyber attacks in real time.

It leverages supervised learning techniques to classify network behavior as **normal** or **attack**, and provides an interactive web interface using Streamlit for user input and instant predictions.

---

## 🚀 Key Features
- 🤖 AI-powered attack detection using Machine Learning  
- 🌐 Real-time prediction with Streamlit web interface  
- 📊 Trained on NSL-KDD dataset  
- ⚡ Fast and lightweight implementation  
- 🧠 Supports anomaly detection based on network behavior  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Framework:** Streamlit  
- **Model:** Random Forest Classifier  

---

## 📂 Project Structure
IDS_Project/ ├── train_model.py      
# Model training script ├── app.py               
# Streamlit web application ├── README.md            
# Project documentation ├── .gitignore           
# Ignore unnecessary files
---

## ⚙️ How It Works
1. Load and preprocess network traffic data  
2. Train ML model to classify traffic  
3. Save trained model (`model.pkl`)  
4. Deploy model using Streamlit UI  
5. User inputs network data → system predicts attack or normal  

---

## ▶️ How to Run

### Step 1: Train the model
```bash
python train_model.py
