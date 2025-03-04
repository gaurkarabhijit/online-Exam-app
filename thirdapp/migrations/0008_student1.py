# Generated by Django 5.1.1 on 2025-01-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0007_delete_student1'),
    ]

    operations = [
        migrations.CreateModel(
            name='student1',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('mobile', models.IntegerField(max_length=15)),
                ('dob', models.DateField()),
                ('course', models.CharField(max_length=50)),
                ('percentages', models.FloatField()),
                ('year_of_study', models.IntegerField()),
            ],
            options={
                'db_table': 'student1',
            },
        ),
    ]
