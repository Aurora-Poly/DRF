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

  # def validate_email(self, obj):
  #       if email_isvalid(obj):
  #         raise serializers.ValidationError('메일 형식이 올바르지 않습니다.')
  #       return obj
        

  # def email_isvalid(email):
  #   try:
  #       validation = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
  #       if re.match(validation, value):
  #           return value
  #       raise Exception('메일 형식이 올바르지 않습니다.')
  #   except Exception as e:
  #       print('예외가 발생했습니다.', e)
