# Generated by Django 5.1.1 on 2025-01-17 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0005_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='student1',
        ),
        migrations.AlterModelTable(
            name='student1',
            table='student1',
        ),
    ]
