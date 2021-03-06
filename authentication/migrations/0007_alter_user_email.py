# Generated by Django 3.2.6 on 2021-08-27 11:38

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True, validators=[authentication.models.validate_email_domain]),
        ),
    ]
