# Generated by Django 2.2.28 on 2022-11-02 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addresswfywismvle'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresswfywismvle',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]