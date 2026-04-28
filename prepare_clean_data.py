import os
import pandas as pd

DATA_DIR = "datasets"
OUTPUT_DIR = os.path.join(DATA_DIR, "cleaned")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def combine_subject_body(df):
    if "subject" in df.columns and "body" in df.columns:
        df["message"] = df["subject"].fillna("") + " " + df["body"].fillna("")
    elif "body" in df.columns:
        df["message"] = df["body"].fillna("")
    else:
        df["message"] = df[df.columns[0]].astype(str)
    return df

#SMS datasets 
sms_files = ["sms.csv", "Spam_SMS.csv"]
sms_data = pd.DataFrame()

for f in sms_files:
    path = os.path.join(DATA_DIR, f)
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    text_col = "message" if "message" in df.columns else df.columns[0]
    label_col = "category" if "category" in df.columns else ("class" if "class" in df.columns else df.columns[-1])
    df = df.rename(columns={text_col: "message", label_col: "label"})
    sms_data = pd.concat([sms_data, df[["message", "label"]]], ignore_index=True)

print(f"📱 SMS data combined: {len(sms_data)} samples")
sms_data.to_csv(os.path.join(OUTPUT_DIR, "sms_data.csv"), index=False)
print(" Saved cleaned SMS data")

#  Email datasets
email_files = [
    "phishing_email.csv", "Enron.csv", "CEAS_08.csv",
    "Ling.csv", "Nigerian_Fraud.csv", "SpamAssasin.csv"
]
email_data = pd.DataFrame()

for f in email_files:
    path = os.path.join(DATA_DIR, f)
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]

    if "text_combined" in df.columns:
        df["message"] = df["text_combined"]
    else:
        df = combine_subject_body(df)

    if "label" not in df.columns:
        df["label"] = "unknown"

    email_data = pd.concat([email_data, df[["message", "label"]]], ignore_index=True)

print(f"✉ Email data combined: {len(email_data)} samples")
email_data.to_csv(os.path.join(OUTPUT_DIR, "email_data.csv"), index=False)
print("✅ Saved cleaned Email data")
