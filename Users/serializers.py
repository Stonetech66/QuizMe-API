from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class RegisterSerializer(RegisterSerializer):
    last_name=serializers.CharField(read_only=True)
    first_name=serializers.CharField(read_only=True)