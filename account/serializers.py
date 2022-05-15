from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    user = User.objects.create_user(
      email = validated_data['email'],
      name = validated_data['name'],
      password = validated_data['password'],
      univ = validated_data['univ'],
      dept = validated_data['dept'],
      age = validated_data['age']
    )
    return  user
  class Meta:
    model = User
    fields = ['email', 'name', 'password', 'univ', 'dept', 'age']