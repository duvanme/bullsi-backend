from rest_framework import serializers
from apiBullsi.models import User, Role

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User     
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'password', 'profile_picture', 'date_of_birth', 'is_active', 'role',
            'created_at', 'updated_at'
        ]

        read_only_fields = ['id', 'created_at', 'updated_at']