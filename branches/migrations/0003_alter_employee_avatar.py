# Generated by Django 4.0.4 on 2023-02-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_employee_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
