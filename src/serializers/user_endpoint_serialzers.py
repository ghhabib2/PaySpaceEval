from rest_framework import serializers


class AddUserSerializer(serializers.Serializer):
    """
    Add User data serializer
    """
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, max_length=128)
    email = serializers.CharField(required=True, max_length=254)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)

class LoggedInUserSerializer(serializers.Serializer):
    """
    Add User data serializer
    """
    user_id = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True, max_length=150)
    email = serializers.CharField(required=True, max_length=254)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)

class LoginUserSerializer(serializers.Serializer):
    """
    Login user Serializer
    """
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, max_length=128)
