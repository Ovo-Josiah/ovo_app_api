from rest_framework import serializers
from signup.models import UserSignUpModel

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignUpModel
        fields = '__all__'
        read_only_fields = ('id',)