import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "datasets", "cleaned")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

#Load SMS and Email cleaned datasets 
sms_path = os.path.join(DATA_DIR, "sms_data.csv")
email_path = os.path.join(DATA_DIR, "email_data.csv")

sms_data = pd.read_csv(sms_path)
email_data = pd.read_csv(email_path)

#Add type labels
sms_data["type"] = "sms"
email_data["type"] = "email"

# Combine and label encode
router_df = pd.concat([sms_data[["message", "type"]], email_data[["message", "type"]]], ignore_index=True)
router_df["type_label"] = router_df["type"].map({"sms": 0, "email": 1})

print(" Router dataset loaded successfully!")
print(router_df["type"].value_counts())

#Train router model 
router_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=4000)),
    ("clf", LogisticRegression(max_iter=200))
])

X_train, X_test, y_train, y_test = train_test_split(
    router_df["message"], router_df["type_label"], test_size=0.2, random_state=42
)

router_pipeline.fit(X_train, y_train)
acc = router_pipeline.score(X_test, y_test)
print(f"Router Model Trained Successfully! Accuracy: {acc*100:.2f}%")

# Save model 
router_path = os.path.join(MODEL_DIR, "router_model.pkl")
joblib.dump(router_pipeline, router_path)

print(f" Router model saved to {router_path}")
