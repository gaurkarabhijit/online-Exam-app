# Generated by Django 5.1.1 on 2025-01-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0012_rename_card_cards_alter_cards_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='short_text',
        ),
        migrations.AlterField(
            model_name='cards',
            name='medium_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cards',
            name='prime_text',
            field=models.CharField(max_length=100),
        ),
    ]
