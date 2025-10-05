# 🚚 Amazon Delivery Time Predictor

A Machine Learning project to **predict delivery times for e-commerce orders** based on multiple factors such as distance, traffic, weather, and agent performance.  
This project includes **data preprocessing, feature engineering, regression modeling, and deployment using Streamlit** with model tracking through **MLflow**.

---

## 🧠 Project Overview

This project aims to estimate the time required to deliver Amazon orders using regression models.  
It involves cleaning and analyzing delivery data, extracting important features, training multiple models, and creating a Streamlit-based prediction app.

---

## 🎯 Objectives

- Predict **delivery time (in hours)** based on various order and delivery factors.  
- Analyze the impact of **traffic**, **weather**, and **agent ratings** on delivery times.  
- Build a **user-friendly interface** to get instant predictions.  
- Track model performance using **MLflow**.  
- Deploy app using **Streamlit + free ngrok tunnel**.

---

## 🧩 Skills Gained

- Python Scripting  
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Regression Modeling (Linear, Random Forest, Gradient Boosting)  
- MLflow Tracking  
- Streamlit App Development  
- Model Deployment

---

## 🧱 Project Architecture

amazon-delivery-time-predictor/
│
├── data/
│ └── amazon_delivery.csv
│
├── models/
│ └── best_model.pkl
│
├── images/
│ ├── app_screenshot1.png
│ └── app_screenshot2.png
│
├── app.py
├── requirements.txt
├── README.md

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python |
| Libraries | pandas, numpy, scikit-learn, matplotlib, seaborn |
| Model Tracking | MLflow |
| Frontend | Streamlit |
| Deployment | Streamlit + ngrok (Free Tunnel) |
| Domain | E-Commerce & Logistics |

---

## 📊 Approach

1. **Data Preparation**
   - Load and clean the dataset (`amazon_delivery.csv`)
   - Handle missing values and outliers  
   - Encode categorical variables

2. **Exploratory Data Analysis (EDA)**
   - Visualize relationships between delivery time, distance, traffic, and weather  
   - Generate feature insights and correlation heatmaps

3. **Feature Engineering**
   - Calculate distance between store and drop coordinates  
   - Extract time-based features (hour, day, etc.)

4. **Model Building**
   - Train and evaluate:
     - Linear Regression  
     - Random Forest Regressor  
     - Gradient Boosting Regressor  
   - Compare metrics: RMSE, MAE, R²  
   - Log all runs in MLflow

5. **App Development**
   - Create a Streamlit app for real-time prediction  
   - Inputs: Agent Age, Rating, Distance, Weather, Traffic  
   - Output: Predicted delivery time (in hours)

6. **Deployment**
   - Deployed Streamlit app using **free ngrok tunnel**

---

## 🧮 Example Output

**Input:**

Agent Age: 25
Agent Rating: 4.0
Weather: Clear
Traffic: Low
Distance: 5.0 km


**Predicted Delivery Time:**


158.60 hours


---

## 🖼️ Application Screenshots

| Streamlit Interface | Prediction Output |
|---------------------|-------------------|
| ![Streamlit App](images/app_screenshot1.png) | ![Prediction Result](images/app_screenshot2.png) |

---

## 🧾 Requirements

To run this project, install dependencies:
```bash
pip install -r requirements.txt

🚀 Run Locally

Clone the repository:

git clone https://github.com/<your-username>/amazon-delivery-time-predictor.git


Navigate to the project folder:

cd amazon-delivery-time-predictor


Run Streamlit app:

streamlit run app.py


To use free hosting:

!ngrok authtoken YOUR_TOKEN
!streamlit run app.py & npx localtunnel --port 8501

📚 Evaluation Metrics

RMSE (Root Mean Square Error)

MAE (Mean Absolute Error)

R² Score (Coefficient of Determination)

🏆 Results

Cleaned and processed dataset ready for modeling

Multiple regression models trained and compared

Streamlit app built for end-user prediction

MLflow used for model tracking and versioning

Successfully deployed app using Streamlit + ngrok

👩‍💻 Author

Rozina Mohsin Pathan
Data Analyst | ML Enthusiast | Streamlit Developer
📧 Email: [rozina8617@gmail.com
]
🌐 GitHub: https://github.com/your-username

