# Generated by Django 2.1.4 on 2019-01-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]