# Generated by Django 4.0.4 on 2023-02-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.FileField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]