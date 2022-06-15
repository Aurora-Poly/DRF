from .models import Resume
from rest_framework import serializers

class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    class Meta:
        model = Resume
        fields = ['user', 'title', 'file_upload', 'date', 'comments']