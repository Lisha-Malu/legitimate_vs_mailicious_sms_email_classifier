import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "datasets", "cleaned")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

#Load cleaned datasets
sms_data = pd.read_csv(os.path.join(DATA_DIR, "sms_data.csv"))
email_data = pd.read_csv(os.path.join(DATA_DIR, "email_data.csv"))

#Add type columns
sms_data["type"] = "sms"
email_data["type"] = "email"

#Combine
router_df = pd.concat([sms_data[["message", "type"]], email_data[["message", "type"]]], ignore_index=True)

#Label encode type
router_df["type_label"] = router_df["type"].map({"sms": 0, "email": 1})

print(" Router data ready:")
print(router_df["type"].value_counts())

#Router Model
router_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("clf", LogisticRegression(max_iter=200))
])

X_router = router_df["message"]
y_router = router_df["type_label"]

router_pipeline.fit(X_router, y_router)
joblib.dump(router_pipeline, os.path.join(MODEL_DIR, "router_model.pkl"))
print("Router model trained and saved!")

# Train SMS Model 
sms_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("clf", LogisticRegression(max_iter=200))
])
sms_pipeline.fit(sms_data["message"], sms_data["label"])
joblib.dump(sms_pipeline, os.path.join(MODEL_DIR, "sms_model.pkl"))
print("SMS model trained and saved!")

#  Train Email Model 
email_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("clf", LogisticRegression(max_iter=200))
])
email_pipeline.fit(email_data["message"], email_data["label"])
joblib.dump(email_pipeline, os.path.join(MODEL_DIR, "email_model.pkl"))
print(" Email model trained and saved!")