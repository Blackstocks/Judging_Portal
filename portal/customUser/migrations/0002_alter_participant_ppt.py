# Generated by Django 4.2.1 on 2023-06-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='ppt',
            field=models.FileField(blank=True, upload_to='presentations/'),
        ),
    ]