# Generated by Django 4.2.5 on 2023-09-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_student_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Time',
            field=models.TimeField(),
        ),
    ]
