# rest_api_app/serializers.py

from rest_framework import serializers
from .models import File, User

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'national_id', 'birth_date', 'address', 'country', 'phone_number', 'email', 'finger_print_signature', 'file']