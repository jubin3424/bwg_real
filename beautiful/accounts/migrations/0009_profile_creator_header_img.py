# Generated by Django 2.0.1 on 2018-02-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_profile_mail_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='creator_header_img',
            field=models.ImageField(blank=True, upload_to='creator/%Y/%m/%d/'),
        ),
    ]
