📌 Overview
This project presents a Machine Learning-based Intrusion Detection System (IDS) designed to identify malicious network traffic and potential cyber attacks in real time.
It leverages supervised learning techniques to classify network behavior as normal or attack, and provides an interactive web interface using Streamlit for user input and instant predictions.
🚀 Key Features
🤖 AI-powered attack detection using Machine Learning
🌐 Real-time prediction with Streamlit web interface
📊 Trained on NSL-KDD dataset
⚡ Fast and lightweight implementation
🧠 Supports anomaly detection based on network behavior
🛠️ Tech Stack
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn
Framework: Streamlit
Model: Random Forest Classifier
📂 Project Structure
IDS_Project/
 ├── train_model.py       # Model training script
 ├── app.py               # Streamlit web application
 ├── README.md            # Project documentation
 ├── .gitignore           # Ignore unnecessary files
⚙️ How It Works
Load and preprocess network traffic data
Train ML model to classify traffic
Save trained model (model.pkl)
Deploy model using Streamlit UI
User inputs network data → system predicts attack or normal
▶️ How to Run
Step 1: Train the model
python train_model.py
Step 2: Launch the application
python -m streamlit run app.py
Step 3: Open in browser
http://localhost:8501
📊 Sample Input
Field
Example
Duration
10
Source Bytes
500
Destination Bytes
1000
Protocol
tcp
Service
http
Flag
SF
📈 Output
✅ Normal Traffic
🚨 Attack Detected
📸 Screenshots
(Add your project screenshots here for better presentation)
🎯 Use Cases
Network security monitoring
SOC (Security Operations Center) analysis
Cyber attack detection and prevention
Educational demonstration of ML in cybersecurity
⚠️ Limitations
Uses simplified input features for demonstration
Accuracy depends on dataset and feature selection
🔮 Future Improvements
Integration with real-time network traffic (e.g., packet capture)
Enhanced UI with dashboards and analytics
Support for advanced ML models (Deep Learning)
Deployment on cloud for public access
👨‍💻 Author
Tharun Kumar
Cybersecurity Enthusiast | Aspiring SOC Analyst
⭐ Acknowledgement
Dataset used: NSL-KDD (Intrusion Detection Dataset)
📌 Conclusion
This project demonstrates how Artificial Intelligence can enhance cybersecurity by automating threat detection and improving response time in modern network environments.
