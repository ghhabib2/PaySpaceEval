from rest_framework import serializers


class TransactionRequestIOSerialize(serializers.Serializer):
    """
    Serializer for Transaction request
    """
    input_address_id = serializers.UUIDField(required=True)
    output_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)

class TransactionRequestIISerialize(serializers.Serializer):
    """
    Serializer for Transaction request
    """
    input_address_id = serializers.UUIDField(required=True)
    output_address_id = serializers.UUIDField(required=True)
    amount = serializers.IntegerField(required=True)

class TransactionResultSerializer(serializers.Serializer):
    """
    Serializer for Transaction result
    """
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(help_text="Output address value")
    block_index = serializers.IntegerField(help_text="Block Index", default=0)
    block_height = serializers.IntegerField(help_text="Block Height", default=0)
    hash = serializers.CharField(help_text="Transaction hash")
    total = serializers.IntegerField(help_text="Total amount", default=0)
    fees = serializers.IntegerField(help_text="Fees", default=0)
    size = serializers.IntegerField(help_text="Size", default=0)
    vsize = serializers.IntegerField(help_text="vSize", default=0)
    preference = serializers.CharField(help_text="Preference", default="")
    relayed_by = serializers.CharField(help_text="Relayed by", default="")
    received = serializers.DateTimeField(help_text="Received time")
    ver = serializers.IntegerField(help_text="ver", default=0)
    double_spend = serializers.BooleanField(help_text="Double Spend flag")
    vin_sz = serializers.IntegerField(help_text="vin_sz", default=0)
    vout_sz = serializers.IntegerField(help_text="vout_sz", default=0)
    confirmations = serializers.IntegerField(help_text="Confirmations")