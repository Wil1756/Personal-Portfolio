# Generated by Django 4.0.4 on 2022-06-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
