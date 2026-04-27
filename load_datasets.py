import os
import pandas as pd

#SETUP
DATA_DIR = "datasets"  # folder containing all 8 datasets
os.makedirs(DATA_DIR, exist_ok=True)

# List all dataset filenames you expect
files = [
    "phishing_email.csv",
    "sms.csv",
    "Spam_SMS.csv",
    "Enron.csv",
    "CEAS_08.csv",
    "Ling.csv",
    "Nigerian_Fraud.csv",
    "SpamAssasin.csv"
]

#  FUNCTION TO LOAD 
def load_dataset(path):
    try:
        df = pd.read_csv(path)
        print(f" Loaded {path} ({len(df)} rows)")
        return df
    except Exception as e:
        print(f"⚠ Error loading {path}: {e}")
        return None

#  LOAD ALL FILES 
datasets = {}
for f in files:
    path = os.path.join(DATA_DIR, f)
    if os.path.exists(path):
        df = load_dataset(path)
        if df is not None:
            datasets[f] = df
    else:
        print(f"⚠ Missing file: {f}")

#  SHOW COLUMN NAMES
print("\n📋 COLUMN SUMMARY:")
for name, df in datasets.items():
    print(f"{name}: {list(df.columns)}")

#SAVE PREVIEW 
preview_path = os.path.join(DATA_DIR, "preview_summary.txt")
with open(preview_path, "w", encoding="utf-8") as f:
    for name, df in datasets.items():
        f.write(f"\n=== {name} ===\n")
        f.write(str(df.head(3)))
        f.write("\n\n")

print(f"\n Saved preview to {preview_path}")