# Phishing Prediction Model

## 📌 Project Overview
Phishing attacks are one of the most common cybersecurity threats where attackers create fake websites to steal sensitive information such as passwords, banking credentials, and personal data.

This project builds a **Machine Learning based Phishing URL Detection System** that predicts whether a given website URL is **legitimate or phishing** based on various URL features.

The goal of this project is to demonstrate how **machine learning can be used in cybersecurity to detect malicious websites automatically.**

---

## 🚀 Features
- Detects whether a URL is **Phishing or Legitimate**
- Uses **Machine Learning classification algorithms**
- Performs **data preprocessing and feature analysis**
- Model training and evaluation
- Simple and easy to understand implementation for beginners

---

## 🧠 Machine Learning Workflow
The project follows the standard machine learning pipeline:

1. **Data Collection**
   - Dataset containing phishing and legitimate URLs.

2. **Data Preprocessing**
   - Cleaning the dataset
   - Handling missing values
   - Feature selection

3. **Feature Extraction**
   URL-based features such as:
   - URL length
   - Presence of special characters
   - Number of subdomains
   - HTTPS usage
   - Domain related features

4. **Model Training**
   - Train machine learning models on the dataset.

5. **Model Evaluation**
   - Evaluate model performance using classification metrics.

6. **Prediction**
   - The trained model predicts whether a URL is phishing or legitimate.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

## 📂 Project Structure

```
Phissing_Prediction_Model
│
├── dataset/                # Dataset used for training
├── notebooks/              # Jupyter notebooks for experimentation
├── model/                  # Trained machine learning model
├── src/                    # Source code
│
├── phishing_detection.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sohail-m09/Phissing_Prediction_Model.git
```

Navigate to the project directory:

```bash
cd Phissing_Prediction_Model
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and execute the cells to:

- Load the dataset
- Train the model
- Evaluate performance
- Predict phishing URLs

---

## 📊 Model Evaluation Metrics

The model performance can be evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

These metrics help measure how well the model detects phishing websites.

---

## 📌 Example Use Case

Input URL:

```
http://secure-login-paypal.com
```

Model Prediction:

```
Phishing Website
```

---

## 🔒 Real World Applications

This type of phishing detection system can be used in:

- Browser security extensions
- Email spam filtering systems
- Banking security systems
- Cybersecurity monitoring tools

---

## 📈 Future Improvements

Possible improvements for the project:

- Use **Deep Learning models**
- Deploy the model using **Flask / FastAPI**
- Create a **web interface for real-time URL checking**
- Improve accuracy with **larger datasets**
- Add **feature engineering for domain analysis**

---

## 👨‍💻 Author

**Momin Sohail Amir**
**B.E Computer**


GitHub:  
https://github.com/Sohail-m09

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.# Phissing_Prediction_Model