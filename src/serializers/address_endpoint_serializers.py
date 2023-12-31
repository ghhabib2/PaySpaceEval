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
    address_id = serializers.UUIDField(required=True)
    address = serializers.CharField(required=True)
    private = serializers.CharField(required=True)
    public = serializers.CharField(required=True)
    wif = serializers.CharField(required=True)

class AddressSearchRequestSerializer(AddressRequestSerializer):
    """
    Address search Request Serializer
    """
    address = serializers.CharField(required=True)

class AddressDetailRequestSerializer(AddressRequestSerializer):
    """
    Address Detail Request Serializer
    """
    address_id = serializers.UUIDField(required=True)

class AddressDetailResultSerializer(AddressResultSerializer):
    address = serializers.CharField(help_text="Wallet Address")
    total_received = serializers.IntegerField(help_text="Total amount received in the Wallet")
    total_sent = serializers.IntegerField(help_text="Total sent by the wallet")
    balance = serializers.IntegerField(help_text="Wallet Balance")
    unconfirmed_balance = serializers.IntegerField(help_text="Nnconfirmed Balance")
    final_balance = serializers.IntegerField(help_text="Final Balace")
    n_tx = serializers.IntegerField(help_text="Number of transactions")
    unconfirmed_n_tx = serializers.IntegerField(help_text="Number of unconfirmed transactions")
    final_n_tx = serializers.IntegerField(help_text="Final transaction")
    tx_url = serializers.CharField(help_text="Transaction Url")
    last_updated = serializers.DateTimeField(help_text="Last update")


class AddressSearchDetailResultSerializer(AddressResultSerializer):
    """
    Address Search Detail Result Serializer
    """
    inner_address = serializers.BooleanField(help_text="Inner address")
    address = serializers.CharField(help_text="Wallet Address")
    total_received = serializers.IntegerField(help_text="Total amount received in the Wallet")
    total_sent = serializers.IntegerField(help_text="Total sent by the wallet")
    balance = serializers.IntegerField(help_text="Wallet Balance")
    unconfirmed_balance = serializers.IntegerField(help_text="Nnconfirmed Balance")
    final_balance = serializers.IntegerField(help_text="Final Balace")
    n_tx = serializers.IntegerField(help_text="Number of transactions")
    unconfirmed_n_tx = serializers.IntegerField(help_text="Number of unconfirmed transactions")
    final_n_tx = serializers.IntegerField(help_text="Final transaction")
    tx_url = serializers.CharField(help_text="Transaction Url")
    last_updated = serializers.DateTimeField(help_text="Last update")