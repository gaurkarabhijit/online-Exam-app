# Generated by Django 5.1.1 on 2025-01-29 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0013_remove_cards_short_text_alter_cards_medium_text_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
