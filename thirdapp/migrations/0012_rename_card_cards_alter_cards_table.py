# Generated by Django 5.1.1 on 2025-01-25 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0011_remove_card_free_text_remove_card_offer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card',
            new_name='Cards',
        ),
        migrations.AlterModelTable(
            name='cards',
            table='Cards',
        ),
    ]
