# Generated by Django 5.1.1 on 2025-01-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0008_student1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student1',
            name='dob',
            field=models.DateField(default=0.00024703557312252963),
        ),
        migrations.AlterField(
            model_name='student1',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
