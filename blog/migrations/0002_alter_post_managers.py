# Generated by Django 5.2.1 on 2025-06-02 02:45

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
