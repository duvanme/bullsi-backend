from rest_framework import serializers
from apiBullsi.models import User, Role

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'profile_picture', 'date_of_birth', 'is_active', 'role',
            'created_at', 'updated_at'
        ]