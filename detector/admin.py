from django.contrib import admin
from .models import PredictionLog

@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'message_type', 'classification', 'summary')
    list_filter = ('message_type','classification')
    search_fields = ('content','summary')