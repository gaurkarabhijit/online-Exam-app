# Generated by Django 5.1.1 on 2025-01-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0010_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='free_text',
        ),
        migrations.RemoveField(
            model_name='card',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='card',
            name='service_text',
        ),
        migrations.AlterField(
            model_name='card',
            name='full_text',
            field=models.CharField(max_length=300),
        ),
    ]
