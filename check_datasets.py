import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "datasets", "cleaned")

sms_path = os.path.join(DATA_DIR, "sms_data.csv")
email_path = os.path.join(DATA_DIR, "email_data.csv")

# Load datasets
sms = pd.read_csv(sms_path)
email = pd.read_csv(email_path)

print("Datasets Loaded Successfully!")
print(f"SMS Samples: {len(sms)} | Email Samples: {len(email)}\n")

# Quick overview
print(" SMS Columns:", sms.columns.tolist())
print(" Email Columns:", email.columns.tolist(), "\n")

#Length statistics
sms["msg_len"] = sms["message"].astype(str).apply(len)
email["msg_len"] = email["message"].astype(str).apply(len)

print(" Average Message Lengths:")
print(f"  SMS Avg Length: {sms['msg_len'].mean():.1f} chars")
print(f"  Email Avg Length: {email['msg_len'].mean():.1f} chars\n")

print(" Label Distribution:")
print("SMS Labels:\n", sms["label"].value_counts(), "\n")
print("Email Labels:\n", email["label"].value_counts(), "\n")

# Example samples
print(" Sample SMS Messages:")
print(sms["message"].head(5).to_string(index=False), "\n")

print(" Sample Email Messages:")
print(email["message"].head(5).to_string(index=False), "\n")

#  Save small preview file
preview_path = os.path.join(DATA_DIR, "data_preview.txt")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write("=== SMS SAMPLES ===\n")
    f.write("\n".join(sms["message"].astype(str).head(10)) + "\n\n")
    f.write("=== EMAIL SAMPLES ===\n")
    f.write("\n".join(email["message"].astype(str).head(10)))
print(f"💾 Preview saved to: {preview_path}")
