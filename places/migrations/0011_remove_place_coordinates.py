# Generated by Django 4.2 on 2024-04-29 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_lat_alter_place_lng'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='coordinates',
        ),
    ]