import uuid
from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    """
    Model for the addresses
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='user_id',
                                help_text="User of the address")
    private = models.CharField(help_text="Private Key", max_length=150)
    public = models.CharField(help_text="Public Key", max_length=150)
    address = models.CharField(help_text="Address", max_length=150)
    wif = models.CharField(help_text="Wallet Import Format", max_length=150)


class AddressInfo(models.Model):
    """
    POCO class for models which also be used for DBF table generation
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE,
                                   related_name='address_id',
                                   help_text="Related Address", null=True, blank=True)
    total_received = models.IntegerField(help_text="Total amount received in the Wallet")
    total_sent = models.IntegerField(help_text="Total sent by the wallet")
    balance = models.IntegerField(help_text="Wallet Balance")
    unconfirmed_balance = models.IntegerField(help_text="Nnconfirmed Balance")
    final_balance = models.IntegerField(help_text="Final Balace")
    n_tx = models.IntegerField(help_text="Number of transactions")
    unconfirmed_n_tx = models.IntegerField(help_text="Number of unconfirmed transactions")
    final_n_tx = models.IntegerField(help_text="Final transaction")
    last_updated = models.DateTimeField(help_text="Last updated time", null=True, blank=True)


class Transaction(models.Model):
    """
    Transaction serializer class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='from_address_id',
                                   help_text="Related Address", null=False, blank=False)
    to_address = models.CharField(max_length=150, help_text="Output address value")
    block_index = models.IntegerField(help_text="Block Index", default=0)
    block_height = models.IntegerField(help_text="Block Height", default=0)
    hash = models.CharField(help_text="Transaction hash")
    total = models.IntegerField(help_text="Total amount", default=0)
    fees = models.IntegerField(help_text="Fees", default=0)
    size = models.IntegerField(help_text="Size", default=0)
    vsize = models.IntegerField(help_text="vSize", default=0)
    preference = models.CharField(help_text="Preference", default="")
    relayed_by = models.CharField(help_text="Relayed by", default="")
    received = models.DateTimeField(help_text="Received time", null=True, blank=True)
    ver = models.IntegerField(help_text="ver", default=0)
    double_spend = models.BooleanField(help_text="Double Spend flag")
    vin_sz = models.IntegerField(help_text="vin_sz", default=0)
    vout_sz = models.IntegerField(help_text="vout_sz", default=0)
    confirmations = models.IntegerField(help_text="Confirmations")

