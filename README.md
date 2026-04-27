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
```
### Step 2: Launch the application
```bash
python -m streamlit run app.py
```
### Step 3: Open in browser
```bash
http://localhost:8501
```
---
## 📊 Sample Input
- Duration: 10
- Source Bytes: 500
- Destination Bytes: 1000
- Protocol: tcp
- Service: http
- Flag: SF
---
## 📈 Output
- ✅ Normal Traffic
- 🚨 Attack Detected
---
## 📸 Screenshots
<img width="1001" height="848" alt="Screenshot 2026-04-27 154403" src="https://github.com/user-attachments/assets/1fca68be-a4c5-4d8e-8292-8b37fb76d31a" />

---

## 🎯 Use Cases
- Network security monitoring
- SOC (Security Operations Center) analysis
- Cyber attack detection and prevention
- Educational demonstration of ML in cybersecurity
---
## ⚠️ Limitations
- Uses simplified input features
- Accuracy depends on dataset
---
## 🔮 Future Improvements
- Real-time packet capture integration
- Advanced dashboard UI
- Deep Learning models
- Cloud deployment
