# Generated by Django 3.2.4 on 2021-06-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210603_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]