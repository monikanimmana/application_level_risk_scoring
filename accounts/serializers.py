from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'username',
            'email',
            'role',
            'risk_score',
            'status',
            'last_ip',
            'last_device',
        ]
        read_only_fields = ['risk_score','last_ip','last_device']