# Generated by Django 5.1.6 on 2025-03-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0003_remove_signup_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Full_name',
            field=models.CharField(max_length=160, null=True),
        ),
    ]
