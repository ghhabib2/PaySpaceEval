# Generated by Django 4.2.2 on 2023-12-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_addressinfo_address_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressinfo',
            name='last_updated',
            field=models.DateTimeField(blank=True, help_text='Last updated time', null=True),
        ),
    ]
