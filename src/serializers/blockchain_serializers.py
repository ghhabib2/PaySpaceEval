from rest_framework import serializers


class Transaction(serializers.Serializer):
    """
    Transaction serializer class
    """
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


class Wallet(serializers.Serializer):
    """
    Wallet serializer class
    """
    address = serializers.CharField(help_text="Wallet Address")
    total_received = serializers.IntegerField(help_text="Total amount received in the Wallet")
    total_sent = serializers.IntegerField(help_text="Total sent by the wallet")
    balance = serializers.IntegerField(help_text="Wallet Balance")
    unconfirmed_balance = serializers.IntegerField(help_text="Nnconfirmed Balance")
    final_balance = serializers.IntegerField(help_text="Final Balace")
    n_tx = serializers.IntegerField(help_text="Number of transactions")
    unconfirmed_n_tx = serializers.IntegerField(help_text="Number of unconfirmed transactions")
    final_n_tx = serializers.IntegerField(help_text="Final transaction")

class Address(serializers.Serializer):
    private = serializers.CharField(help_text="Private Key")
    public = serializers.CharField(help_text="Public Key")
    address = serializers.CharField(help_text="Address")
    wif = serializers.CharField(help_text="Wallet Import Format")


class UnsignedTransaction(serializers.Serializer):
    input_address = serializers.CharField(help_text="Input Address")
    output_address = serializers.CharField(help_text="Output Address")
    value = serializers.IntegerField(help_text="Value")




