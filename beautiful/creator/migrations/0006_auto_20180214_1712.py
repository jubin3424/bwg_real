# Generated by Django 2.0.1 on 2018-02-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='item/%Y/%m/%d'),
        ),
    ]