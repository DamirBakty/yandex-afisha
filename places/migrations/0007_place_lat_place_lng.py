# Generated by Django 4.2 on 2024-04-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_place_description_long_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
