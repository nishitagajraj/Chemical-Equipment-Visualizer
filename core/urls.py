from django.urls import path
from .views import EquipmentAnalysisView
from . import views

urlpatterns = [
    path('upload/', EquipmentAnalysisView.as_view(), name='file-upload'),
    path('api/export-pdf/', views.export_pdf),
]