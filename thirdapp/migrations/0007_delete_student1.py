# Generated by Django 5.1.1 on 2025-01-17 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0006_rename_student_student1_alter_student1_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student1',
        ),
    ]
