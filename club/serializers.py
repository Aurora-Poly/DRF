from .models import Club
from rest_framework import serializers

class ClubSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    class Meta:
        model = Club
        fields =['id','user', 'title', 'name', 'personnel', 'content', 'date']