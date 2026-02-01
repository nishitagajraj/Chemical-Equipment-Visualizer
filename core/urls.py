from django.urls import path
from .views import EquipmentAnalysisView

urlpatterns = [
    path('upload/', EquipmentAnalysisView.as_view(), name='file-upload'),
]