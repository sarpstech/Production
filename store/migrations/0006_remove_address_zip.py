# Generated by Django 3.2.24 on 2024-02-08 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20240205_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='zip',
        ),
    ]
