# Generated by Django 5.1.2 on 2025-01-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_alter_app_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='admin_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
