# Generated by Django 3.1.5 on 2021-01-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='short_url',
        ),
        migrations.AlterField(
            model_name='link',
            name='long_url',
            field=models.TextField(unique=True, verbose_name='URL'),
        ),
    ]
