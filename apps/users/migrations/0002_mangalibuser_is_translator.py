# Generated by Django 4.2.6 on 2023-11-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangalibuser',
            name='is_translator',
            field=models.BooleanField(default=False),
        ),
    ]