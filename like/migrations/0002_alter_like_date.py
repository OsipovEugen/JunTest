# Generated by Django 3.2.6 on 2021-10-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
