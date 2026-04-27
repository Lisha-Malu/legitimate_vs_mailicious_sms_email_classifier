from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.history, name='history'),
    path('delete/<int:id>/', views.delete_history, name='delete_history'),
    path('export_excel/', views.export_to_excel, name='export_excel'),
]

