# Generated by Django 5.1.2 on 2024-11-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_otp_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='business_registration',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='permission_letter',
        ),
        migrations.AddField(
            model_name='developer',
            name='business_registration_number',
            field=models.CharField(default='UNKNOWN', max_length=100),
        ),
        migrations.AddField(
            model_name='developer',
            name='city',
            field=models.CharField(default='UNKNOWN', max_length=100),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization_address',
            field=models.CharField(default='UNKNOWN', max_length=255),
        ),
        migrations.AddField(
            model_name='developer',
            name='organization_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='sub_city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='woreda',
            field=models.CharField(default='UNKNOWN', max_length=100),
        ),
        migrations.AddField(
            model_name='developer',
            name='zone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='organization_name',
            field=models.CharField(default='UNKNOWN', max_length=255),
        ),
    ]
