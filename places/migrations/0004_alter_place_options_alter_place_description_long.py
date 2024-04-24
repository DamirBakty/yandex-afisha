# Generated by Django 4.2 on 2024-04-24 05:17

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_placeimage_options_alter_placeimage_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]