# Generated by Django 3.2.6 on 2021-08-27 13:52

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210827_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, validators=[authentication.validators.validate_last_name]),
        ),
    ]