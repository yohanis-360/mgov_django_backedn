from rest_framework import serializers
from .models import User, Developer

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'mobile_number', 'date_of_birth', 'gender']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DeveloperRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = [
            'organization_name',
            'organization_address',
            'organization_website',
            'city',
            'woreda',
            'zone',
            'sub_city',
            'business_registration_number',  
            'status'
            ]
