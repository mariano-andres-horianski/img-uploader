# Generated by Django 3.2.12 on 2022-04-13 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
