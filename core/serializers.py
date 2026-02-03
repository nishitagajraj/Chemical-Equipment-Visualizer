from rest_framework import serializers
from .models import EquipmentUpload

class EquipmentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentUpload
        fields = ['id', 'file', 'uploaded_at']