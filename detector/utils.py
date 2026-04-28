from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl
import joblib
import os

# Load ML Models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

router_model = joblib.load(os.path.join(MODEL_DIR, "router_model.pkl"))
sms_model = joblib.load(os.path.join(MODEL_DIR, "sms_model.pkl"))
email_model = joblib.load(os.path.join(MODEL_DIR, "email_model.pkl"))

#  Home Page 
def index(request):
    prediction_result = None
    msg_type = None

    if request.method == "POST":
        message = request.POST.get("message", "")
        category = request.POST.get("category", "")

        if not message or not category:
            prediction_result = "⚠️ Please enter a message and select a category"
        else:
            model = sms_model if category == "sms" else email_model

            # Try probability-based prediction
            try:
                spam_prob = model.predict_proba([message])[0][1]
            except:
                pred = model.predict([message])[0]
                spam_prob = 1 if int(pred) == 1 else 0

            threshold = 0.4

            spam_keywords = [
                "win", "claim", "reward", "offer", "free", "lottery",
                "urgent", "click", "verify", "bank", "password", "update"
            ]
            rule_based_flag = any(word in message.lower() for word in spam_keywords)

            if spam_prob > threshold or rule_based_flag:
                prediction_result = "🚨 Phishing / Fraudulent"
            else:
                prediction_result = "✅ Legitimate / Safe"

            msg_type = "SMS" if category == "sms" else "Email"

            # Save to session history (latest 5 messages)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history = request.session.get("history", [])
            history.insert(0, {
                "message": message,
                "type": msg_type,
                "result": prediction_result,
                "time": timestamp
            })
            request.session["history"] = history[:5]

    history = request.session.get("history", [])
    return render(request, "detector/index.html", {
        "prediction": prediction_result,
        "type": msg_type,
        "history": history
    })


# Dashboard Page 
def dashboard(request):
    history = request.session.get("history", [])
    total_checks = len(history)
    phishing_count = sum(1 for h in history if "Phishing" in h["result"])
    safe_count = total_checks - phishing_count

    return render(request, "detector/dashboard.html", {
        "total_checks": total_checks,
        "phishing_count": phishing_count,
        "safe_count": safe_count,
        "history": history
    })


#History Page 
def history(request):
    history = request.session.get("history", [])
    return render(request, "detector/history.html", {"history": history})


# Delete History Item
def delete_history(request, id):
    history = request.session.get("history", [])
    if 0 <= id < len(history):
        del history[id]
        request.session["history"] = history
    return redirect("history")


# Export to Excel 
def export_to_excel(request):
    history = request.session.get("history", [])
    if not history:
        return HttpResponse("No data to export")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Fraud Detection History"

    ws.append(["Message", "Type", "Result", "Timestamp"])
    for record in history:
        ws.append([
            record["message"],
            record["type"],
            record["result"],
            record["time"]
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="fraud_history.xlsx"'

    wb.save(response)
    return response
