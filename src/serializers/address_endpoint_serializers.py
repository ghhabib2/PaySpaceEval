from rest_framework import serializers

class AddressRequestSerializer(serializers.Serializer):
    """
    Address Request Serializer
    """
    user_id = serializers.IntegerField(read_only=True)

class AddressResultSerializer(serializers.Serializer):
    """
    Address Result Serializer
    """
    address = serializers.CharField(required=True)
    private = serializers.CharField(required=True)
    public = serializers.CharField(required=True)
    wif = serializers.CharField(required=True)