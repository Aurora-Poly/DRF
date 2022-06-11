from .models import Portfolio
from rest_framework import serializers

class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.name')
    class Meta:
        model = Portfolio
        fields = ['user','title', 'content', 'date', 'head_img', 'file_upload']