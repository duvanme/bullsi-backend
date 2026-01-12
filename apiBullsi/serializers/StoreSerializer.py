from rest_framework import serializers
from apiBullsi.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id', 'name', 'address', 'phone_number', 'email',
            'created_at', 'updated_at', 'user_id'
        ]
        read_only_fields = ['user_id', 'created_at', 'updated_at']