from rest_framework import serializers


class Transaction(serializers.ModelSerializer):
    """
    Transaction serializer class
    """
    class Meta:
        # model = TransAction # TODO: Will work on it later
        fields = '__all__'

    tx_hash = serializers.CharField(help_text="Transaction hash")
    block_height = serializers.IntegerField(help_text="Block Height")
    tx_input_n = serializers.IntegerField(help_text="Transaction input number")
    tx_output_n = serializers.IntegerField(help_text="Transaction output number")
    value = serializers.IntegerField(help_text="value")
    ref_balance = serializers.IntegerField(help_text="Ref balance")
    spent = serializers.BooleanField(help_text="Spent flag")
    confirmations = serializers.IntegerField(help_text="Confirmations")
    confirmed = serializers.DateTimeField("Confirmation Date and Time")
    double_spend = serializers.BooleanField(help_text="Double Spend flag")

class Wallet(serializers.ModelSerializer):
    """
    Wallet serializer class
    """
    class Meta:
        # model = Wallet # TODO: Will work on it later
        fields = '__all__'

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
    txrefs = Transaction(many=True, read_only=True)

class Address(serializers.Serializer):
    private = serializers.CharField(help_text="Private Key")
    public = serializers.CharField(help_text="Public Key")
    address = serializers.CharField(help_text="Address")
    wif = serializers.CharField(help_text="Wallet Import Format")




