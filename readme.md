# 📧 Phishing Email Detection System
A machine learning-based phishing email detection system with a Django web interface that allows users
to classify emails as phishing or legitimate, view prediction history, explore analytics dashboards,
and download reports in Excel format.

Live project link:
https://legitimate-vs-mailicious-sms-email.onrender.com/

#🚀 Features
# 🔍 Email & SMS Classification
* Input email, sms text and get real-time prediction (Phishing / Safe)
* Probability/confidence score for each prediction
* Feature-based ML model

# 🧠 Machine Learning Pipeline
* Feature extraction from email text:
  * Word statistics (words, unique words, stopwords)
  * Link & domain analysis
  * Email address detection
  * Spelling error estimation
  * Urgency keyword detection
* Handles class imbalance using SMOTE
* Trained using Naive Bayes Classifier

# 🌐 Django Web Interface
* Clean and simple UI for email & SMS testing
* Real-time prediction system
* Responsive design for usability

# 📊 Dashboard
* Visual analytics of predictions
* Distribution of phishing vs safe emails
* Performance insights from logged data

# 📜 Prediction History
* Stores all past predictions
* Displays:
  * Email text
  * Prediction result
  * Confidence score
  * Timestamp

# 📁 Excel Report Export
* Download prediction history as Excel file
* Useful for analysis and reporting

# 🏗️ Project Architecture
Email Input (Django UI)
        ↓
Feature Extraction (NLP Pipeline)
        ↓
ML Model (Naive Bayes + SMOTE)
        ↓
Prediction Output
        ↓
Database Logging (History)
        ↓
Dashboard & Excel Export

# 🧰 Tech Stack
* Backend:Django 
* Machine Learning: scikit-learn, imbalanced-learn (SMOTE)
* NLP: NLTK, TextBlob
* Data Processing: Pandas, NumPy
* Frontend: HTML, CSS, Bootstrap ( Django Templates)
* Export: openpyxl

# 📦 Installation
1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Run Django server

# 📊 Dataset
The model can be trained using datasets:
* Ethan Cratchley Email Phishing Dataset (Kaggle)
* Naseer Abdullah Alam Phishing Dataset (Kaggle)

#📌 Future Improvements
* Integrate BERT-based deep learning model
* Real-time email scanning via IMAP integration
* URL reputation checking
* Advanced phishing pattern detection


# 👨‍💻 Author
Lisha Malu

Built as a machine learning + Django project for phishing email, SMS detection and analysis.

