# Generated by Django 5.1.2 on 2024-10-10 20:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Unknown', max_length=100)),
                ('last_name', models.CharField(default='Unknown', max_length=100)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='Unknown', max_length=50)),
                ('password', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
    ]
