# Generated by Django 2.0.1 on 2018-02-11 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mail_subscription',
        ),
    ]
