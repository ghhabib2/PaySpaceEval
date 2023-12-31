# Generated by Django 4.2.2 on 2023-12-31 01:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_addressinfo_tx_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('to_address', models.CharField(help_text='Output address value', max_length=150)),
                ('tx_hash', models.CharField(help_text='Transaction hash')),
                ('block_height', models.IntegerField(help_text='Block Height')),
                ('tx_input_n', models.IntegerField(help_text='Transaction input number')),
                ('tx_output_n', models.IntegerField(help_text='Transaction output number')),
                ('value', models.IntegerField(help_text='value')),
                ('ref_balance', models.IntegerField(help_text='Ref balance')),
                ('spent', models.BooleanField(help_text='Spent flag')),
                ('confirmations', models.IntegerField(help_text='Confirmations')),
                ('confirmed', models.DateTimeField(verbose_name='Confirmation Date and Time')),
                ('double_spend', models.BooleanField(help_text='Double Spend flag')),
                ('from_address_id', models.ForeignKey(blank=True, help_text='Related Address', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_address_id', to='app.address')),
            ],
        ),
    ]