# Generated by Django 2.0.1 on 2018-01-30 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='item',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
