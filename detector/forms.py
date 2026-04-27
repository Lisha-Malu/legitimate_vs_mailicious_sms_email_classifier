# detector/forms.py
from django import forms

class PredictionForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'placeholder': 'Paste SMS or Email body here...'}), label="Message")
    summary = forms.CharField(required=False, max_length=255, label="One-line summary (optional)")